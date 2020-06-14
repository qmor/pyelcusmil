import unittest
from .MilDevice import MilPacket, Mil1553Device, MilPacketFormat
import time

'''This test is using for test MilDevice work in BusController mode. You need at least two Mil1553 cards to run this test
first one for BC
second one for RT
'''


class TestBCFormat1(unittest.TestCase):
    def __init__(self):
        self.packetRT = MilPacket()
        self.packetBC = MilPacket()
        self.packetBC.commandWord = 0xffff

    def listenerRt(self, packet):
        self.packetRT = packet

    def listenerBC(self, packet):
        self.packetBC = packet

    def test(self):
        device1 = Mil1553Device(cardnumber=0)
        device1.init_as(mode="BC")
        device1.addListener(self.listenerBC)
        device2 = Mil1553Device(cardnumber=1)
        device2.init_as(mode="RT", rtaddress=15)
        device2.addListener(self.listenerRt)
        device2.setPause(False)
        packet = MilPacket()
        packet.commandWord = MilPacket.makeCW(15, 0, 16, 0)
        for i in range(32):
            packet.dataWords[i] = i * 2
        device1.sendpacket(packet)
        time.sleep(2)
        self.assertEquals(self.packetRT.commandWord, self.packetBC.commandWord)
        self.assertEquals(self.packetRT.format, MilPacketFormat.CC_FMT_1)
        self.assertEquals(self.packetBC.format, MilPacketFormat.CC_FMT_1)