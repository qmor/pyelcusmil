from MilDevice import Mil1553Device
import sys

device = Mil1553Device()
device.init_as(mode="BC")
