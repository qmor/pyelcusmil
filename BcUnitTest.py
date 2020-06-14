import unittest
from .MilDevice import MilPacket, Mil1553Device, MilPacketFormat
import time
import random
'''This test is using for test MilDevice work in BusController mode. You need at least two Mil1553 cards to run this test
first one for BC
second one for RT
'''


class TestBCFormat1(unittest.TestCase):


    def listenerRt(self, packet):
        self.packetRT = MilPacket.createCopy(packet)
        print("RT received")

    def listenerBC(self, packet):
        self.packetBC = MilPacket.createCopy(packet)
        print("BC received")

    def test(self):
        self.packetRT = None
        self.packetBC = None


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
            packet.dataWords[i] = random.randrange(0,0xffff)
        device1.sendpacket(packet)
        time.sleep(1)
        self.assertEqual(self.packetRT.commandWord, self.packetBC.commandWord & 0x7ff)
        self.assertEqual(self.packetRT.format, MilPacketFormat.CC_FMT_1)
        self.assertEqual(self.packetBC.format, MilPacketFormat.CC_FMT_1)
        print(self.packetBC)
        print(self.packetRT)
        for i in range(32):
            self.assertEqual(self.packetBC.dataWords[i], self.packetRT.dataWords[i])
