import sys
from enum import Enum

is_windows = sys.platform.startswith('win')
if not is_windows:
    try:
        from .driverLinux import Mil1553LinuxDriver as MilDriver
    except:
        from driverLinux import Mil1553LinuxDriver as MilDriver
else:
    from .driverWindows import Mil1553WindowsDriver as MilDriver
from ctypes import Structure
import ctypes
from threading import Thread
import threading
import datetime
import queue

try:
    from .TTmkEventData import TTmkEventData
except:
    from TTmkEventData import TTmkEventData
import time


class ElcusAnsBits:
    ANS_BIT_SREQ = 0x01
    ANS_BIT_BUSY = 0x02
    ANS_BIT_SSFL = 0x04
    ANS_BIT_RTFL = 0x08
    ANS_BIT_DNBA = 0x10


class ElcusConst:
    RT_ENABLE = 0x0000
    RT_DISABLE = 0x001F
    RT_GET_ENABLE = 0xFFFF
    CX_NOSIG = 0x0000
    CX_SIG = 0x8000
    CX_INT = 0x0000
    CX_NOINT = 0x0020
    CX_CONT = 0x0010
    RT_TRANSMIT = 0x0400
    RT_RECEIVE = 0x0000
    RT_ERROR_MASK = 0x4000
    S_ERAO_MASK = 0x01
    S_MEO_MASK = 0x02
    S_IB_MASK = 0x04
    S_TO_MASK = 0x08
    S_EM_MASK = 0x10
    S_EBC_MASK = 0x20
    S_DI_MASK = 0x40
    S_ELN_MASK = 0x80
    S_G1_MASK = 0x1000
    S_G2_MASK = 0x2000
    DATA_BC_RT = 0x00
    DATA_BC_RT_BRCST = 0x08
    DATA_RT_BC = 0x01
    DATA_RT_RT = 0x02
    DATA_RT_RT_BRCST = 0x0A
    CTRL_C_A = 0x03
    CTRL_C_BRCST = 0x0B
    CTRL_CD_A = 0x04
    CTRL_CD_BRCST = 0x0C
    CTRL_C_AD = 0x05
    RT_HBIT_MODE = 0x0001
    RT_FLAG_MODE = 0x0002
    RT_BRCST_MODE = 0x0004
    RT_DATA_BL = 0x2000
    RT_GENER1_BL = 0x0004
    RT_GENER2_BL = 0x4000
    BC_GENER1_BL = 0x0004
    BC_GENER2_BL = 0x4000
    MT_GENER1_BL = 0x0004
    MT_GENER2_BL = 0x4000
    TMK_IRQ_OFF = 0x8000


class MilErrorCodes(Enum):
    SX_NOERR = 0
    SX_MEO = 1
    SX_TOA = 2
    SX_TOD = 3
    SX_ELN = 4
    SX_ERAO = 5
    SX_ESYN = 6
    SX_EBC = 7


class MilPacketStatus(Enum):
    NEW = 0
    SENT = 1
    RECEIVED = 2
    FAILED = 3


class MilPacketBus(Enum):
    BUS_A = 0
    BUS_B = 1


class MilPacketFormat(Enum):
    CC_FMT_1 = 0x0
    CC_FMT_2 = 0x1
    CC_FMT_3 = 0x02
    CC_FMT_4 = 0x03
    CC_FMT_5 = 0x05
    CC_FMT_6 = 0x04
    CC_FMT_7 = 0x08
    CC_FMT_8 = 0x0a
    CC_FMT_9 = 0x0b
    CC_FMT_10 = 0x0c
    CC_FMT_UNKNOWN = 0xff


class TTmkConfigData(Structure):
    _pack_ = 1
    _fields_ = [("nType", ctypes.c_uint16),
                ("szname", ctypes.c_uint8 * 10),
                ("wPorts1", ctypes.c_uint16),
                ("wPorts2", ctypes.c_uint16),
                ("wIrq1", ctypes.c_uint16),
                ("wIrq2", ctypes.c_uint16),
                ("wIODelay", ctypes.c_uint16)]

    def __str__(self):
        s = ''.join([chr(i) for i in self.szname]).rstrip('\x00')
        return "nType %04x\r\nszname %s\r\nwPorts1 %04x\r\nwPorts2 %04X\r\nwIrq1 %04X\r\nwIrq2 %04x\r\nwIODelay %04X\r\n" % (
            self.nType, s, self.wPorts1, self.wPorts2, self.wIrq1, self.wIrq2, self.wIODelay)


class MilPacket(Structure):
    _fields_ = [("commandWord", ctypes.c_uint16),
                ("dataWords", ctypes.c_uint16 * 32),
                ("answerWord", ctypes.c_uint16)]

    def __str__(self):
        res = ""
        res += "date: " + str(self.date) + "\r\n"
        res += "status: " + str(self.status) + "\r\n"
        res += "errorcode: " + str(self.errorcode) + "\r\n"
        res += 'CW %04X\r\n' % self.commandWord
        res += 'format:%s\r\n' % str(self.format)
        res += 'AW %04X\r\n' % self.answerWord
        res += " ".join(["%04X" % i for i in self.dataWords]) + "\r\n"
        return res

    def __init__(self):
        self.format = MilPacketFormat.CC_FMT_UNKNOWN
        self.date = datetime.datetime.now()
        self.status = MilPacketStatus.NEW
        self.bus = MilPacketBus.BUS_A
        self.errorcode = MilErrorCodes.SX_NOERR

    @staticmethod
    def createCopy(packet):
        res = MilPacket()
        res.commandWord = packet.commandWord
        res.answerWord = packet.answerWord
        for i in range(32):
            res.dataWords[i] = packet.dataWords[i]
        res.format = packet.format
        res.date = packet.date
        res.status = packet.status
        res.bus = packet.bus
        res.errorcode = packet.errorcode
        return res

    @staticmethod
    def createFromRaw(pBuffer, sw, statusword):
        res = MilPacket()
        res.date = datetime.datetime.now()
        res.bus = 1 if (((sw & 0xffff) >> 15) == 1) else 0
        res.commandWord = pBuffer[0]
        # this.sw = rawPacket.sw;
        res.errorcode = sw & 7
        res.errorcode = MilErrorCodes(res.errorcode)

        res.status = MilPacketStatus.RECEIVED

        if res.errorcode != MilErrorCodes.SX_NOERR:
            res.status = MilPacketStatus.FAILED

        res.format = MilPacket.calcFormat(res.commandWord)
        i = MilPacket.getWordsCount(res.commandWord)
        if i == 0:
            i = 32

        if res.format == MilPacketFormat.CC_FMT_1:
            for m in range(i):
                res.dataWords[m] = pBuffer[m + 1]
            res.answerWord = pBuffer[i + 1]
        elif res.format == MilPacketFormat.CC_FMT_2:
            res.answerWord = pBuffer[1]
            for m in range(i):
                res.dataWords[m] = pBuffer[2 + m]
        elif res.format == MilPacketFormat.CC_FMT_4:
            res.answerWord = pBuffer[1]
        elif res.format == MilPacketFormat.CC_FMT_5:
            res.answerWord = pBuffer[1]
            res.dataWords[0] = pBuffer[2]
        elif res.format == MilPacketFormat.CC_FMT_6:
            res.answerWord = pBuffer[2]
            res.dataWords[0] = pBuffer[1]
        return res

    @staticmethod
    def getWordsCount(cmdWord):
        return cmdWord & 0x1f

    @staticmethod
    def getRTRBit(cmdWord):
        return (cmdWord >> 10) & 0x1

    @staticmethod
    def getSubAddress(cmdWord):
        return (cmdWord >> 5) & 0x1f

    @staticmethod
    def getRtAddress(cmdWord):
        return (cmdWord & 0xffff) >> 11

    @staticmethod
    def makeCW(a, rtr, sa, wc):
        return a << 11 | rtr << 10 | sa << 5 | wc

    @staticmethod
    def calcFormat(cmdword):
        address = MilPacket.getRtAddress(cmdword)
        rtrbit = MilPacket.getRTRBit(cmdword)
        subaddress = MilPacket.getSubAddress(cmdword)
        wordscount = MilPacket.getWordsCount(cmdword)
        isItMode = True if (subaddress == 0 or subaddress == 0x1f) else False
        if rtrbit == 0 and not isItMode and address != 31:
            return MilPacketFormat.CC_FMT_1

        elif rtrbit == 1 and not isItMode and address != 31:
            return MilPacketFormat.CC_FMT_2

        elif rtrbit == 1 and isItMode and (0 <= wordscount <= 15) and address != 31:
            return MilPacketFormat.CC_FMT_4

        elif rtrbit == 1 and isItMode and (wordscount == 16 or wordscount == 18 or wordscount == 19):
            return MilPacketFormat.CC_FMT_5

        elif rtrbit == 0 and isItMode and (wordscount == 17 or wordscount == 20 or wordscount == 21):
            return MilPacketFormat.CC_FMT_6

        elif address == 31 and not isItMode and rtrbit == 0:
            return MilPacketFormat.CC_FMT_7

        return MilPacketFormat.CC_FMT_UNKNOWN


class Mil1553Device:
    lock = threading.Lock()

    def innerlistenloopMT(self, list):
        while self.threadRunning:
            if not list.empty():
                packet = list.get()
                for listener in self.listeners:
                    listener(MilPacket.createCopy(packet))
            else:
                time.sleep(0.05)

    def listenloopRT(self):
        eventData = TTmkEventData()
        pBuffer = (ctypes.c_uint16 * 64)()
        waitingtime = 10
        while self.threadRunning:
            passed = False
            events = self.driver.tmkwaitevents(1 << self.cardnumber, waitingtime)
            if events == (1 << self.cardnumber):
                passed = True
            if passed:
                with self.lock:
                    self.driver.tmkselect(self.cardnumber)
                    self.driver.tmkgetevd(eventData)
                    Msg = MilPacket()
                    if eventData.nInt == 1:  # rtIntCmd
                        Msg.answerWord = 0
                        Msg.commandWord = eventData.union.rt.wStatus
                        Msg.format = MilPacket.calcFormat(Msg.commandWord)
                        for i in range(32):
                            Msg.dataWords[i] = 0
                        Msg.dataWords[0] = self.driver.rtgetcmddata(Msg.commandWord & 31)
                        Msg.status = MilPacketStatus.RECEIVED

                        answElcus = self.driver.rtgetanswbits()
                        if (answElcus & 0x1) == ElcusAnsBits.ANS_BIT_SREQ:
                            Msg.answerWord |= 1 << 8
                        if (answElcus & 0x2) == ElcusAnsBits.ANS_BIT_BUSY:
                            Msg.answerWord |= 1 << 3
                        if (answElcus & 0x4) == ElcusAnsBits.ANS_BIT_SSFL:
                            Msg.answerWord |= 1 << 2
                        if (answElcus & 0x8) == ElcusAnsBits.ANS_BIT_RTFL:
                            Msg.answerWord |= 1
                        if (answElcus & 0x10) == ElcusAnsBits.ANS_BIT_DNBA:
                            Msg.answerWord |= 1 << 1

                        for listener in self.listeners:
                            listener(MilPacket.createCopy(Msg))

                    elif eventData.nInt == 2:  # rtIntErr
                        raise Exception("Error in listenloopRT")

                    elif eventData.nInt == 3:  # rtIntData
                        Msg.commandWord = eventData.union.rt.wStatus
                        Msg.format = MilPacket.calcFormat(Msg.commandWord)
                        self.driver.rtdefsubaddr(
                            ElcusConst.RT_RECEIVE if (
                                    MilPacket.getRTRBit(Msg.commandWord) == 0) else ElcusConst.RT_TRANSMIT,
                            MilPacket.getSubAddress(Msg.commandWord))
                        ln = MilPacket.getWordsCount(Msg.commandWord)
                        if ln == 0:
                            ln = 32

                        self.driver.rtgetblk(0, pBuffer, ln)
                        for i in range(ln):
                            Msg.dataWords[i] = pBuffer[i]
                        Msg.status = MilPacketStatus.RECEIVED

                        answElcus = self.driver.rtgetanswbits()
                        if (answElcus & 0x1) == ElcusAnsBits.ANS_BIT_SREQ:
                            Msg.answerWord |= 1 << 8
                        if (answElcus & 0x2) == ElcusAnsBits.ANS_BIT_BUSY:
                            Msg.answerWord |= 1 << 3
                        if (answElcus & 0x4) == ElcusAnsBits.ANS_BIT_SSFL:
                            Msg.answerWord |= 1 << 2
                        if (answElcus & 0x8) == ElcusAnsBits.ANS_BIT_RTFL:
                            Msg.answerWord |= 1
                        if (answElcus & 0x10) == ElcusAnsBits.ANS_BIT_DNBA:
                            Msg.answerWord |= 1 << 1

                        for listener in self.listeners:
                            listener(MilPacket.createCopy(Msg))

    def listenloopMT(self):
        lst = queue.Queue()
        listenerThread = threading.Thread(target=self.innerlistenloopMT, args=(lst,))
        listenerThread.setDaemon(True)
        listenerThread.start()
        waitingtime = 10
        eventData = TTmkEventData()
        pBuffer = (ctypes.c_uint16 * 64)()
        while self.threadRunning:
            passed = False
            events = self.driver.tmkwaitevents(1 << self.cardnumber, waitingtime)
            if events == (1 << self.cardnumber):
                passed = True
            if passed:
                with self.lock:
                    self.driver.tmkselect(self.cardnumber)
                    self.driver.tmkgetevd(eventData)
                    if eventData.nInt == 3:
                        pass
                    elif eventData.nInt == 4:
                        self.driver.mtdefbase(self.mtLastBase)
                        self.mtLastBase = ((self.mtLastBase + 1) & self.mtMaxBase)
                        sw = self.driver.mtgetsw()
                        statusword = eventData.union.mt.wResultX
                        self.driver.mtgetblk(0, pBuffer, 64)
                        packet = MilPacket.createFromRaw(pBuffer, sw, statusword)

                        lst.put(MilPacket.createCopy(packet))

    def listenloopBC(self):

        eventData = TTmkEventData()
        pBuffer = (ctypes.c_uint16 * 64)()
        while self.threadRunning:
            passed = False
            events = self.driver.tmkwaitevents(1 << self.cardnumber, 100)
            if events == (1 << self.cardnumber):
                passed = True
            if passed:
                with self.lock:
                    Msg = MilPacket()
                    res = self.driver.tmkselect(self.cardnumber)
                    if res != 0:
                        print("tmkselect: ", res)

                    self.driver.tmkgetevd(eventData)
                    res = self.driver.bcdefbase(0)
                    if res != 0:
                        print("bcdefbase: ", res)
                    Msg.commandWord = self.driver.bcgetw(0)
                    Msg.format = MilPacket.calcFormat(Msg.commandWord)
                    Msg.date = datetime.datetime.now()
                    cmdcodeWordCount = MilPacket.getWordsCount(Msg.commandWord)
                    if Msg.format == MilPacketFormat.CC_FMT_1:
                        wordcount = cmdcodeWordCount
                        if wordcount == 0:
                            wordcount = 32
                        self.driver.bcgetblk(1, pBuffer, wordcount)
                        for i in range(wordcount):
                            Msg.dataWords[i] = pBuffer[i]
                        Msg.answerWord = self.driver.bcgetw(1 + wordcount)
                    elif Msg.format == MilPacketFormat.CC_FMT_2:
                        wordcount = cmdcodeWordCount
                        if wordcount == 0:
                            wordcount = 32
                        self.driver.bcgetblk(2, pBuffer, wordcount)
                        for i in range(wordcount):
                            Msg.dataWords[i] = pBuffer[i]
                        Msg.answerWord = self.driver.bcgetw(1)

                    elif Msg.format == MilPacketFormat.CC_FMT_4:
                        Msg.answerWord = self.driver.bcgetw(1)
                    elif Msg.format == MilPacketFormat.CC_FMT_5:
                        Msg.answerWord = self.driver.bcgetw(1)
                        Msg.dataWords[0] = self.driver.bcgetw(2)

                    elif Msg.format == MilPacketFormat.CC_FMT_6:
                        Msg.answerWord = self.driver.bcgetw(2)
                        Msg.dataWords[0] = self.driver.bcgetw(1)

                    if eventData.nInt == 1:
                        Msg.status = MilPacketStatus.RECEIVED

                    elif eventData.nInt == 2:
                        Msg.status = MilPacketStatus.FAILED
                    else:
                        pass
                        #print("EventData.nInt ",eventData.nInt)

                        if eventData.union.bc.wResult == ElcusConst.S_ERAO_MASK:
                            Msg.errorcode = "The error in a field of the address received RW is found out"

                        elif eventData.union.bc.wResult == ElcusConst.S_MEO_MASK:
                            Msg.errorcode = "The error of a code 'Manchester - 2' is found out at answer RT"

                        elif eventData.union.bc.wResult == ElcusConst.S_EBC_MASK:
                            Msg.errorcode = "The error of the echo - control over transfer BC is found out"

                        elif eventData.union.bc.wResult == ElcusConst.S_TO_MASK:
                            Msg.errorcode = "It is not received the answer from RT"

                        elif eventData.union.bc.wResult == ElcusConst.S_IB_MASK:
                            Msg.errorcode = "The established bits in received RW are found out"

                    for listener in self.listeners:
                        listener(MilPacket.createCopy(Msg))

            if not self.packetsForSendBC.empty():
                msg = self.packetsForSendBC.get()
                msg.format = MilPacket.calcFormat(msg.commandWord)
                with self.lock:
                    res = self.driver.tmkselect(self.cardnumber)
                    if res != 0:
                        print("tmkselect: ", res)
                    if msg.format == MilPacketFormat.CC_FMT_1:
                        pBuffer[0] = msg.commandWord
                        for i in range(32):
                            pBuffer[i + 1] = msg.dataWords[i]

                        self.driver.bcdefbase(0)
                        self.driver.bcputblk(0, pBuffer, 64)
                        self.driver.bcdefbus(msg.bus)
                        self.driver.bcstart(0, ElcusConst.DATA_BC_RT)
                        self.bcsent += 1
                        msg.status = MilPacketStatus.SENT
                    elif msg.format == MilPacketFormat.CC_FMT_2:
                        res = self.driver.bcdefbase(0)
                        if res != 0:
                            print("bcdefbase: ", res)
                        self.driver.bcputw(0, msg.commandWord)
                        res = self.driver.bcdefbus(msg.bus)
                        if res != 0:
                            print("bcdefbus: ", res)
                        res = self.driver.bcstart(0, ElcusConst.DATA_RT_BC)
                        if res != 0:
                            print("bcstart: " + res)
                        self.bcsent += 1
                        msg.status = MilPacketStatus.SENT

                    elif msg.format == MilPacketFormat.CC_FMT_4 or msg.format == MilPacketFormat.CC_FMT_5:
                        self.driver.bcdefbase(0)
                        self.driver.bcputw(0, msg.commandWord)
                        self.driver.bcdefbus(msg.bus)
                        self.driver.bcstart(0, msg.format.value)
                        self.bcsent += 1
                        msg.status = MilPacketStatus.SENT

                    elif msg.format == MilPacketFormat.CC_FMT_6:
                        self.driver.bcdefbase(0)
                        self.driver.bcputw(0, msg.commandWord)
                        self.driver.bcputw(1, msg.dataWords[0])
                        self.driver.bcdefbus(msg.bus)
                        self.driver.bcstart(0, msg.format.value)
                        self.bcsent += 1
                        msg.status = MilPacketStatus.SENT

    def __init__(self, cardnumber=0):
        self.cardnumber = cardnumber
        self.driver = MilDriver()
        self.packetsForSendBC = queue.Queue()
        self.mode = None
        self.bcsent = 0
        self.listeners = []
        self.mtLastBase = 0
        self.mtMaxBase = 0
        self.paused = False
        self.rtaddress = 0
        self.threadRunning = False
        self.runnerThread = None

    def startmt(self, mtBase, mtCtrlCode):
        if self.paused:
            res = self.driver.mtstartx(mtBase, mtCtrlCode)
            if res == 0:
                self.paused = False

    def stopmt(self):
        if not self.paused:
            res = self.driver.mtstop()
            if res == 0:
                self.paused = True

    def addListener(self, listener):
        self.listeners.append(listener)

    def sendPacketRT(self, packet):
        with self.lock:
            result = self.driver.tmkselect(self.cardnumber)
            if result != 0:
                raise Exception("Ошибка tmkselect в sendPacketRT ", result)
            subaddressMode = MilPacket.getSubAddress(packet.commandWord)
            rtrBit = MilPacket.getRTRBit(packet.commandWord)
            wordcountModeCode = MilPacket.getWordsCount(packet.commandWord)
            if rtrBit == 1:
                if subaddressMode != 0 and subaddressMode != 31:
                    if wordcountModeCode == 0:
                        wordcountModeCode = 32
                    self.driver.rtdefsubaddr(ElcusConst.RT_TRANSMIT, subaddressMode)
                    while self.driver.rtbusy() == 1:
                        time.sleep(0.01)
                    self.driver.rtputblk(0, packet.dataWords, wordcountModeCode)
                else:  # if Mode
                    self.driver.rtputcmddata((packet.commandWord & 31) | (1 << 10), packet.dataWords[0])  # first  dataword is   for CMD data

    def sendpacket(self, packet):
        if self.mode == 'BC':
            self.packetsForSendBC.put(packet)
        elif self.mode == "RT":
            self.sendPacketRT(packet)

    def done(self):
        result = self.driver.tmkdone(self.cardnumber)
        return result

    def init_as(self, mode="BC", rtaddress=0, verbose=False):
        result = self.driver.tmk_open()
        if result != 0:
            raise ("Ошибка TmkOpen ", result)
        result = self.driver.tmkconfig(self.cardnumber)
        if result != 0:
            raise Exception("Ошибка tmkconfig ", result)
        configData = TTmkConfigData()
        self.driver.tmkgetinfo(configData)
        if verbose:
            print(configData)
        result = self.driver.tmkselect(self.cardnumber)
        if result != 0:
            raise Exception("Ошибка tmkselect ", result)
        if mode == "BC":
            result = self.driver.bcreset()
            if result != 0:
                raise Exception("Ошибка bcreset() ", result)

            result |= self.driver.bcdefirqmode(ElcusConst.RT_GENER1_BL | ElcusConst.RT_GENER2_BL)

            if result != 0:
                raise Exception("Ошибка bcdefirqmode() ", result)
            self.runnerThread = Thread(target=self.listenloopBC, daemon=True)
        elif mode == "MT":
            result = self.driver.mtreset()
            if result != 0:
                raise Exception("Ошибка mtreset ", result)
            result |= self.driver.mtdefirqmode(ElcusConst.RT_GENER1_BL | ElcusConst.RT_GENER2_BL)
            if result != 0:
                raise Exception("Ошибка mtdefirqmode() ", result)
            self.mtMaxBase = self.driver.mtgetmaxbase()
            for i in range(self.mtMaxBase):
                self.driver.mtdefbase(i)
                self.driver.mtdeflink(i + 1, ElcusConst.CX_CONT | ElcusConst.CX_NOINT | ElcusConst.CX_SIG)
            self.stopmt()
            self.runnerThread = Thread(target=self.listenloopMT, daemon=True)
            self.startmt(0, ElcusConst.CX_CONT | ElcusConst.CX_NOINT | ElcusConst.CX_NOSIG)
        elif mode == "RT":
            result = self.driver.rtreset()
            if result != 0:
                raise ("Ошибка rtreset ", result)
            result = self.driver.rtdefaddress(rtaddress)
            if result != 0:
                raise ("Ошибка rtdefaddress ", result)
            self.rtaddress = rtaddress
            result = self.driver.rtdefmode(0)
            result |= self.driver.rtdefirqmode(0)
            self.driver.rtenable(ElcusConst.RT_DISABLE)
            self.runnerThread = Thread(target=self.listenloopRT, daemon=True)

        else:
            raise ("Unknown mode ", mode)
        self.threadRunning = True
        self.runnerThread.start()
        self.mode = mode

    def isEnabled(self):
        isEnbl = self.driver.rtenable(ElcusConst.RT_GET_ENABLE)
        return True if (isEnbl == ElcusConst.RT_ENABLE) else False

    def setPause(self, pause):
        if self.mode == "RT":
            with self.lock:
                result = self.driver.tmkselect(self.cardnumber)
                if result != 0:
                    raise Exception("Ошибка tmkselect в функции setPause() ", result)

            if self.isEnabled() == pause:
                result = self.driver.rtenable(ElcusConst.RT_DISABLE if self.isEnabled() else ElcusConst.RT_ENABLE)
                if result != 0:
                    raise Exception("Ошибка rtenable в функции setPause() ", result)

            elif self.mode == "MT":
                with self.lock:
                    result = self.driver.tmkselect(self.cardnumber)
                    if result != 0:
                        raise Exception("Ошибка tmkselect в функции setPause() ", result)

                    result = self.stopmt() if pause else self.startmt(self.mtLastBase, (
                            ElcusConst.CX_CONT | ElcusConst.CX_NOINT | ElcusConst.CX_NOSIG))

                    if result != 0:
                        raise Exception("Ошибка startmt/stopmt в функции setPause() ", result)

            if pause:
                self.threadRunning = False
                self.runnerThread.join()
            elif not self.threadRunning:
                self.runnerThread = Thread(target=self.listenloopMT, daemon=True)
