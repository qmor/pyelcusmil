import driverLinux
from driverLinux import Mil1553LinuxDriver
from ctypes import Structure
import ctypes

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


class MilPacket(Structure):
    _fields_ = [("CommandWord", ctypes.c_uint16),
                ("DataWords", ctypes.c_uint16 * 32),
                ("AnswerWords", ctypes.c_uint16)]


class Mil1553Device:
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
            self.mode =mode