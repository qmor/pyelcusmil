import unittest
from .MilDevice import MilPacket, Mil1553Device, MilPacketFormat, MilPacketStatus
import time
import random

'''This test is using for test MilDevice work in BusController mode. You need at least two Mil1553 cards to run this test
first one for BC
second one for RT
'''

class TestBcFormat6(unittest.TestCase):
    def listenerBC(self, packet):
        #print("listenerBC")
        self.packetBC = packet

    def listenerRT(self, packet):
        self.packetRT = packet
        print(self.packetRT)
        print("listenerRT")

    def setUp(self):
        self.packetRT = None
        self.packetBC = None
        self.device1 = Mil1553Device(cardnumber=0)
        self.device1.init_as(mode="BC")
        self.device1.addListener(self.listenerBC)
        self.device2 = Mil1553Device(cardnumber=1)
        self.device2.init_as(mode="RT", rtaddress=15)
        self.device2.addListener(self.listenerRT)
        self.device2.setPause(False)

    def tearDown(self):
        self.device1.done()
        self.device2.done()

    def test(self):
        packet = MilPacket()
        packet.commandWord = MilPacket.makeCW(15, 0, 31, 17)  # команда - sync
        packet.dataWords[0] = 0x1488
        self.device1.sendpacket(packet)
        time.sleep(2)
        self.assertIsNotNone(self.packetBC)
        self.assertIsNotNone(self.packetRT)
        self.assertEqual(self.packetRT.format, MilPacketFormat.CC_FMT_6)
        self.assertEqual(self.packetRT.status, MilPacketStatus.RECEIVED)
        self.assertEqual(self.packetRT.dataWords[0], 0x1488)


class TestBcFormat5(unittest.TestCase):
    def listenerBC(self, packet):
        #print("listenerBC")
        self.packetBC = packet

    def listenerRT(self, packet):
        #print("listenerRT")
        pass

    def setUp(self):
        self.packetRT = None
        self.packetBC = None
        self.device1 = Mil1553Device(cardnumber=0)
        self.device1.init_as(mode="BC")
        self.device1.addListener(self.listenerBC)
        self.device2 = Mil1553Device(cardnumber=1)
        self.device2.init_as(mode="RT", rtaddress=15)
        self.device2.addListener(self.listenerRT)
        self.device2.setPause(False)
        packet =MilPacket()
        packet.commandWord = MilPacket.makeCW(15, 1, 31, 16)  # команда - передать ВС
        packet.dataWords[0] = 0x1488
        self.device2.sendpacket(packet)

    def tearDown(self):
        self.device1.done()
        self.device2.done()

    def test(self):
        packet = MilPacket()
        packet.commandWord = MilPacket.makeCW(15, 1, 31, 16)  # команда - передать ВС
        self.device1.sendpacket(packet)
        time.sleep(1)
        self.assertEqual(self.packetBC.format, MilPacketFormat.CC_FMT_5)
        self.assertEqual(self.packetBC.dataWords[0], 0x1488)
        self.assertEqual(MilPacketStatus.RECEIVED, self.packetBC.status)

class TestBcFormat4(unittest.TestCase):
    def listenerBC(self, packet):
        #print("listenerBC")
        self.packetBC = packet

    def listenerRT(self, packet):
        #print("listenerRT")
        pass

    def setUp(self):
        self.packetRT = None
        self.packetBC = None
        self.device1 = Mil1553Device(cardnumber=0)
        self.device1.init_as(mode="BC")
        self.device1.addListener(self.listenerBC)
        self.device2 = Mil1553Device(cardnumber=1)
        self.device2.init_as(mode="RT", rtaddress=15)
        self.device2.addListener(self.listenerRT)
        self.device2.setPause(False)

    def tearDown(self):
        self.device1.done()
        self.device2.done()

    def test(self):
        packet = MilPacket()
        packet.commandWord = MilPacket.makeCW(15, 1, 31, 2)  # команда - передать ОС
        self.device1.sendpacket(packet)
        time.sleep(1)
        self.assertEqual(self.packetBC.format, MilPacketFormat.CC_FMT_4)
        self.assertEqual(self.packetBC.status, MilPacketStatus.RECEIVED)

class TestBcFormat2(unittest.TestCase):
    def listenerBC(self, packet):
        self.packetBC = MilPacket.createCopy(packet)
        # print("BC received")

    def listenerRt(self, packet):
        # print("RT received")
        pass

    def setUp(self):
        self.packetRT = MilPacket()
        self.packetRT.commandWord = MilPacket.makeCW(15, 1, 16, 0)
        self.packetRT.format = MilPacket.calcFormat(self.packetRT.commandWord)
        for i in range(32):
            self.packetRT.dataWords[i] = random.randrange(0, 0xffff)
        self.device1 = Mil1553Device(cardnumber=0)
        self.device1.init_as(mode="BC")
        self.device1.addListener(self.listenerBC)
        self.device2 = Mil1553Device(cardnumber=1)
        self.device2.init_as(mode="RT", rtaddress=15)
        self.device2.addListener(self.listenerRt)
        self.device2.setPause(False)
        self.device2.sendpacket(self.packetRT)

    def test(self):
        packet = MilPacket()
        packet.commandWord = self.packetRT.commandWord
        self.device1.sendpacket(packet)
        time.sleep(1)
        self.assertEqual(self.packetRT.commandWord, self.packetBC.commandWord)
        self.assertEqual(self.packetRT.format, MilPacketFormat.CC_FMT_2)
        self.assertEqual(self.packetBC.format, MilPacketFormat.CC_FMT_2)
        # print(self.packetBC)
        # print(self.packetRT)
        for i in range(32):
            self.assertEqual(self.packetBC.dataWords[i], self.packetRT.dataWords[i])

    def tearDown(self):
        self.device1.done()
        self.device2.done()


class TestBCFormat1(unittest.TestCase):
    def setUp(self):
        self.packetRT = None
        self.packetBC = None
        self.device1 = Mil1553Device(cardnumber=0)
        self.device1.init_as(mode="BC")
        self.device1.addListener(self.listenerBC)
        self.device2 = Mil1553Device(cardnumber=1)
        self.device2.init_as(mode="RT", rtaddress=15)
        self.device2.addListener(self.listenerRt)
        self.device2.setPause(False)

    def tearDown(self):
        self.device1.done()
        self.device2.done()

    def listenerRt(self, packet):
        self.packetRT = MilPacket.createCopy(packet)
        # print("RT received")

    def listenerBC(self, packet):
        self.packetBC = MilPacket.createCopy(packet)
        # print("BC received")

    def test(self):

        packet = MilPacket()
        packet.commandWord = MilPacket.makeCW(15, 0, 16, 0)
        for i in range(32):
            packet.dataWords[i] = random.randrange(0, 0xffff)
        self.device1.sendpacket(packet)
        time.sleep(1)
        self.assertEqual(self.packetRT.commandWord, self.packetBC.commandWord & 0x7ff)
        self.assertEqual(self.packetRT.format, MilPacketFormat.CC_FMT_1)
        self.assertEqual(self.packetBC.format, MilPacketFormat.CC_FMT_1)
        # print(self.packetBC)
        # print(self.packetRT)
        for i in range(32):
            self.assertEqual(self.packetBC.dataWords[i], self.packetRT.dataWords[i])
