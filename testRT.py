from MilDevice import Mil1553Device
from MilDevice import MilPacket
import time
import sys

def receiverListener(packet):
    print("Packet ", packet.date)
    print(packet.format)
    print("CW %04X" %packet.commandWord)
    print("AW %04X" %packet.answerWord)
    print(" ".join(["%04X"%i for i in packet.dataWords]))


device = Mil1553Device(cardnumber=4)
device.init_as(mode="RT", rtaddress=1)
device.addListener(receiverListener)
device.setPause(False)
packet = MilPacket()
packet.commandWord = 0xc20
for i in range(32):
    packet.dataWords[i] = i+1
device.sendpacket(packet)
while True:
    time.sleep(1)