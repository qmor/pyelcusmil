import driverLinux
from driverLinux import Mil1553LinuxDriver
from ctypes import Structure
import ctypes
from threading import Thread
import threading
import datetime
import queue
from driverLinux import TTmkEventData

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

    def __init__(self):
        self.format = None
        self.date = datetime.datetime.now()
        self.status = None
        self.bus = 0
        self.errorcode = ""
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
    def calcFormat(cmdword):
        rtrbit = MilPacket.getRTRBit(cmdword)
        subaddress = MilPacket.getSubAddress(cmdword)
        wordscount = MilPacket.getWordsCount(cmdword)
        isItMode = True if (subaddress == 0 or subaddress == 0x1f) else False
        if rtrbit == 0 and not isItMode:
            return "CC_FMT_1"

        elif rtrbit == 1 and not isItMode:
            return "CC_FMT_2"

        elif rtrbit == 1 and isItMode and (0 <= wordscount <= 15):
            return "CC_FMT_4"

        elif rtrbit == 1 and isItMode and (wordscount == 16 or wordscount == 18 or wordscount == 19):
            return "CC_FMT_5"

        elif rtrbit == 0 and isItMode and (wordscount == 17 or wordscount == 20 or wordscount == 21):
            return "CC_FMT_6"

        return None




class Mil1553Device:

    def listenloopBC(self):

        events = 0
        eventData = TTmkEventData()
        Msg = MilPacket()
        pBuffer = (ctypes.c_uint16*64)()
        passed = True
        while self.threadRunning:
            passed = False
            events = self.driver.tmkwaitevents(1 << self.cardnumber, 100)
            if events == (1 << self.cardnumber):
                passed = True
            if passed:
                with threading.Lock():
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
                    if Msg.format == "CC_FMT_1":
                        wordcount = cmdcodeWordCount
                        if wordcount == 0:
                            wordcount = 32
                        self.driver.bcgetblk(1, pBuffer, wordcount)
                        for i in range(wordcount):
                            Msg.dataWords[i] = pBuffer[i]
                        Msg.answerWord = self.driver.bcgetw(1 + wordcount)
                    elif Msg.format == "CC_FMT_2":
                        wordcount = cmdcodeWordCount
                        if wordcount == 0:
                            wordcount = 32
                        self.driver.bcgetblk(2, pBuffer, wordcount)
                        for i in range(wordcount):
                            Msg.dataWords[i] = pBuffer[i]
                        Msg.answerWord = self.driver.bcgetw(1)

                    elif Msg.format == "CC_FMT_4":
                        Msg.answerWord = self.driver.bcgetw(1)
                    elif Msg.format == "CC_FMT_5":
                        Msg.answerWord = self.driver.bcgetw(1)
                        Msg.dataWords[0] = self.driver.bcgetw(2)


                    elif Msg.format == "CC_FMT_6":
                        Msg.answerWord = self.driver.bcgetw(2)
                        Msg.dataWords[0] = self.driver.bcgetw(1)

                    if eventData.nInt == 1:
                        Msg.status = "Received"

                    if eventData.nInt == 2:
                        Msg.status = "Failed"

                        if eventData.union.bc.wResult == S_ERAO_MASK:
                            Msg.errorcode = "The error in a field of the address received RW is found out"

                        elif eventData.union.bc.wResult == S_MEO_MASK:
                            Msg.errorcode = "The error of a code 'Manchester - 2' is found out at answer RT"

                        elif eventData.union.bc.wResult == S_EBC_MASK:
                            Msg.errorcode = "The error of the echo - control over transfer BC is found out"

                        elif eventData.union.bc.wResult == S_TO_MASK:
                            Msg.errorcode = "It is not received the answer from RT"

                        elif eventData.union.bc.wResult == S_IB_MASK:
                            Msg.errorcode = "The established bits in received RW are found out"

                    for listener in self.listeners:
                        listener(MilPacket.createCopy(Msg))

            if not self.packetsForSendBC.empty():
                msg = self.packetsForSendBC.get()
                msg.format = MilPacket.calcFormat(msg.commandWord)
                with threading.Lock():
                    res = self.driver.tmkselect(self.cardnumber)
                    if res != 0:
                        print("tmkselect: ", res)
                    if msg.format == "CC_FMT_1":
                        pBuffer[0] = msg.commandWord
                        for i in range(32):
                            pBuffer[i+1] = msg.dataWords[i]

                        self.driver.bcdefbase(0)
                        self.driver.bcputblk(0, pBuffer, 64)
                        self.driver.bcdefbus(msg.bus)
                        self.driver.bcstart(0, DATA_BC_RT)
                        self.bcsent += 1
                        msg.status = "SENT"
                    elif msg.format == "CC_FMT_2":
                        res = self.driver.bcdefbase(0)
                        if res != 0:
                            print("bcdefbase: ", res)
                        self.driver.bcputw(0, msg.commandWord)
                        res = self.driver.bcdefbus(msg.bus)
                        if res != 0:
                            print("bcdefbus: ", res)
                        res = self.driver.bcstart(0, DATA_RT_BC)
                        if res != 0:
                            print("bcstart: " + res)
                        self.bcsent += 1
                        msg.status = "SENT"

                    elif msg.format == "CC_FMT_4" or msg.format == "CC_FMT_5":
                        self.driver.bcdefbase(0)
                        self.driver.bcputw(0, msg.commandWord)
                        self.driver.bcdefbus(msg.bus)
                        self.driver.bcstart(0, msg.format.asInteger())
                        self.bcsent += 1
                        msg.status = "SENT"


                    elif msg.format == "CC_FMT_6":
                        self.driver.bcdefbase(0)
                        self.driver.bcputw(0, msg.commandWord)
                        self.driver.bcputw(1, msg.dataWords[0])
                        self.driver.bcdefbus(msg.bus)
                        self.driver.bcstart(0, msg.format.asInteger())
                        self.bcsent += 1
                        msg.status = "SENT"

    def __init__(self, cardnumber=0):
        self.cardnumber = cardnumber
        self.driver = Mil1553LinuxDriver()
        self.packetsForSendBC = queue.Queue()
        self.mode = None
        self.bcsent = 0
        self.listeners = []

    def addListener(self, listener):
        self.listeners.append(listener)

    def sendpacket(self, packet):
        if self.mode == 'BC':
            self.packetsForSendBC.put(packet)

    def init_as(self, mode="BC"):
        result = self.driver.tmk_open()
        if result != 0:
            raise ("Ошибка TmkOpen ", result)
        result = self.driver.tmkconfig(self.cardnumber)
        if result != 0:
            raise ("Ошибка tmkconfig ", result)
        configData = TTmkConfigData()
        self.driver.tmkgetinfo(configData)
        print(configData)
        result = self.driver.tmkselect(self.cardnumber)
        if result != 0:
            raise ("Ошибка tmkselect ", result)
        if mode == "BC":
            result = self.driver.bcreset()
            if result != 0:
                raise ("Ошибка bcreset() ", result)

            result |= self.driver.bcdefirqmode(RT_GENER1_BL | RT_GENER2_BL)

            if result != 0:
                raise ("Ошибка bcdefirqmode() ", result)
            self.runnerThread = Thread(target=self.listenloopBC, daemon=True)
            self.threadRunning = True
            self.runnerThread.start()
            self.mode = mode
