from MilDevice import Mil1553Device
from MilDevice import MilPacket
import sys

device = Mil1553Device()
device.init_as(mode="BC")
msg = MilPacket()
msg.commandWord = 1 << 11 | 0 << 10 | 1 << 5 | 1
device.sendpacket(msg)
sleep(1)
