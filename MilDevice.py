import driverLinux
from driverLinux import Mil1553LinuxDriver
from ctypes import Structure
import ctypes
from threading import Thread
import threading
RT_GENER1_BL = 0x0004
RT_GENER2_BL = 0x4000


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


class BC(Structure):
    _fields_=[("wResult",ctypes.c_uint16),
              ("wAW1",ctypes.c_uint16),
              ("wAW2",ctypes.c_uint16)]

class EventDataUnion(ctypes.Union):
    _fields_=[("BC",BC)]

class TTmkEventData(Structure):
    _fields_=[("nInt",ctypes.c_uint32),
              ("wMode",ctypes.c_uint16),
              ("Union",EventDataUnion)]


class MilPacket(Structure):
    _fields_ = [("CommandWord", ctypes.c_uint16),
                ("DataWords", ctypes.c_uint16 * 32),
                ("AnswerWords", ctypes.c_uint16)]


class Mil1553Device:

    def listenloopBC(self):
        events = 0
        eventData = TTmkEventData()
        Msg = MilPacket()
        pBuffer = bytes(128)
        passed = True
        res = 0
        while self.threadRunning == True:
                passed = False
                events = self.driver.tmkwaitevents(1 << self.cardnumber, 100)
            if events == (1 << self.cardnumber):
                passed = True
            if passed:
                with threading.Lock():
                    res=self.driver.tmkselect(self.cardnumber)
            if (res != 0) {
            System.out.println("tmkselect: "+res);
            }
            driver.tmkgetevd(eventData);
            res=driver.bcdefbase((short) 0);
            if (res != 0) {
            System.out.println("bcdefbase: "+res);
            }
            Msg.commandWord =  driver.bcgetw((short) 0);
            Msg.format = Mil1553Packet.calcFormat(Msg.commandWord);
            Msg.date = LocalDateTime.now();
            short cmdcodeWordCount = Mil1553Packet.getWordsCount(Msg.commandWord);
            switch(Msg.format)
            {
            case CC_FMT_1:
                driver.bcgetblk((short)
            1, pBuffer, cmdcodeWordCount);
            Msg.dataWords = pBuffer.getShortArray(0, 32);
            Msg.answerWord = driver.bcgetw((short)(1 + cmdcodeWordCount));
        break;
        case
        CC_FMT_2:
        int
        wordcount = cmdcodeWordCount;
        if (wordcount == 0)
            wordcount = 32;

        driver.bcgetblk((short)
        2, pBuffer, (short)
        wordcount);
        Msg.dataWords = pBuffer.getShortArray(0, 32);
        Msg.answerWord = driver.bcgetw((short)
        1);
        break;

    case
    CC_FMT_4:
    Msg.answerWord = driver.bcgetw((short)
    1);
    break;


case
CC_FMT_5:
Msg.answerWord = driver.bcgetw((short)
1);
Msg.dataWords[0] = driver.bcgetw((short)
2);
break;
case
CC_FMT_6:
Msg.answerWord = driver.bcgetw((short)
2);
Msg.dataWords[0] = driver.bcgetw((short)
1);
break;
default:
break;
}
if (eventData.nInt == 1)
{

// if (!packetsForSendBC.isEmpty())
// packetsForSendBC.remove(0);

Msg.status = EMilPacketStatus.eRECEIVED;
}

if (eventData.nInt == 2)
{
Msg.status = EMilPacketStatus.eFAILED;
// if (!packetsForSendBC.isEmpty())
// {
   // packetsForSendBC.clear();
//}
if (eventData.union.bc.wResult == S_ERAO_MASK)
    for (DebugReceivedListener listener: DebugReceivedListeners)
        {
            listener.msgReceived("The error in a field of the address received RW is found out");
        }
        else if (eventData.union.bc.wResult == S_MEO_MASK)
            for (DebugReceivedListener listener: DebugReceivedListeners)
                {
                    listener.msgReceived("The error of a code 'Manchester - 2' is found out at answer RT");
                }
                else if (eventData.union.bc.wResult == S_EBC_MASK)
                    for (DebugReceivedListener listener: DebugReceivedListeners)
                        {
                            listener.msgReceived("The error of the echo - control over transfer BC is found out");
                        }
                        else if (eventData.union.bc.wResult == S_TO_MASK)
                            for (DebugReceivedListener listener: DebugReceivedListeners)
                                {
                                    listener.msgReceived("It is not received the answer from RT");
                                }
                                else if (eventData.union.bc.wResult == S_IB_MASK)
                                    for (DebugReceivedListener listener: DebugReceivedListeners)
                                        {
                                            listener.msgReceived("The established bits in received RW are found out");
                                        }
                                    }
                                    for (IMilMsgReceivedListener listener: msgReceivedListeners)
                                    {
                                        listener.msgReceived(new
                                        Mil1553Packet(Msg));
                                        }
                                        }
                                        }
                                        if (!packetsForSendBC.isEmpty())
                                        {
                                        Mil1553Packet msg = packetsForSendBC.poll();
                                        msg.format = Mil1553Packet.calcFormat(msg.commandWord);
                                        synchronized (syncObject) {
                                        res=driver.tmkselect(cardNumber);
                                        if (res != 0) {
                                        System.out.println("tmkselect: " + res);
                                    }
                                    if (msg.format == EMilFormat.CC_FMT_1)
                                    {
                                    pBuffer.setShort(0, msg.commandWord);
                                    for (int i=0;i < 32;i++)
                                        pBuffer.setShort(i * 2 + 2, msg.dataWords[i]);

                                    driver.bcdefbase((short)
                                    0);
                                    driver.bcputblk((short)
                                    0, pBuffer, (short)
                                    64);
                                    driver.bcdefbus(msg.bus.toInt());
                                    driver.bcstart((short)
                                    0, (short)
                                    DATA_BC_RT);
                                    bcsent + +;
                                    msg.status = EMilPacketStatus.eSENT;
                                }
                                else if (msg.format.equals(EMilFormat.CC_FMT_2))
                                {
                                res = driver.bcdefbase((short)
                                0);
                                if (res != 0) {
                                System.out.println("bcdefbase: "+res);
                                }
                                driver.bcputw((short)
                                0, msg.commandWord);
                                res = driver.bcdefbus(msg.bus.toInt());
                                if (res != 0) {
                                System.out.println("bcdefbus: "+res);
                                }
                                res = driver.bcstart((short)
                                0, (short)
                                DATA_RT_BC);
                                if (res != 0) {
                                System.out.println("bcstart: "+res);
                                }
                                bcsent + +;
                                msg.status = EMilPacketStatus.eSENT;
                            }
                            else if (msg.format.equals(EMilFormat.CC_FMT_4) | | msg.format.equals(EMilFormat.CC_FMT_5))
                            {
                            driver.bcdefbase((short)
                            0);
                            driver.bcputw((short)
                            0, msg.commandWord);
                            driver.bcdefbus((msg.bus.toInt()));
                            driver.bcstart((short)
                            0, msg.format.asInteger());
                            bcsent + +;
                            msg.status = EMilPacketStatus.eSENT;
                        }

                        else if (msg.format.equals(EMilFormat.CC_FMT_6))
                        {
                        driver.bcdefbase((short)
                        0);
                        driver.bcputw((short)
                        0, msg.commandWord);
                        driver.bcputw((short)
                        1, msg.dataWords[0]);
                        driver.bcdefbus(msg.bus.toInt());
                        driver.bcstart((short)
                        0, msg.format.asInteger());
                        bcsent + +;
                        msg.status = EMilPacketStatus.eSENT;
                    }
                    else
                    {
                    // packetsForSendBC.remove(0);
                    for (DebugReceivedListener listener: DebugReceivedListeners)
                        {
                            listener.msgReceived("Exchange format is not realized yet");
                        }
                        }
                        }
                        }
                        }

    def __init__(self, cardnumber=0):
        self.cardnumber = cardnumber
        self.driver = Mil1553LinuxDriver()
        self.mode = None
    def sendpacket(self, packet):
        if (self.mode=='BC'):
            pass

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
        if (mode == "BC"):
            result = self.driver.bcreset()
            if result != 0:
                raise ("Ошибка bcreset() ", result)

            result |= self.driver.bcdefirqmode(RT_GENER1_BL | RT_GENER2_BL)

            if result != 0:
                raise ("Ошибка bcdefirqmode() ", result)
            self.runnerThread = Thread(target= self.listenloopBC,daemon=True )
            self.threadRunning = True
            self.mode = mode