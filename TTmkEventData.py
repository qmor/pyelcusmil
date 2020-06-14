import ctypes
class BC_(ctypes.Structure):
    _fields_ = [("wResult", ctypes.c_uint16),
                ("wAW1", ctypes.c_uint16),
                ("wAW2", ctypes.c_uint16)]


class BCX_(ctypes.Structure):
    _fields_ = [("wBase", ctypes.c_uint16),
                ("wResultX", ctypes.c_uint16)]


class RT_(ctypes.Structure):
    _fields_ = [("wStatus", ctypes.c_uint16),
                ("wCmd", ctypes.c_uint16)]


class MT_(ctypes.Structure):
    _fields_ = [("wBase", ctypes.c_uint16),
                ("wResultX", ctypes.c_uint16)]


class MRT_(ctypes.Structure):
    _fields_ = [("wStatus", ctypes.c_uint16)]


class TMK_(ctypes.Structure):
    _fields_ = [("wRequest", ctypes.c_uint16)]

class TTmkEventData(ctypes.Structure):

    class EventDataUnion(ctypes.Union):
        _fields_ = [("bc", BC_),
                    ("bcx", BCX_),
                    ("rt", RT_),
                    ("mt", MT_),
                    ("mrt", MRT_),
                    ("tmk", TMK_)]

    _fields_=[("nInt",ctypes.c_uint32),
              ("wMode",ctypes.c_uint16),
              ("union",EventDataUnion)]