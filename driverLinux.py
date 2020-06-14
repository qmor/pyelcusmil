from .LTMK import ioctl
import fcntl
import os
import ctypes
from ctypes import CDLL

libc = CDLL("libc.so.6")






def ioctrext(fd,cmd,arg):
    result = libc.ioctl(fd, cmd, arg)
    return  result
def ioctl_(fd, cmd, arg):
    result = 0
    try:
        result = fcntl.ioctl(fd, cmd, arg)
        #result = libc.ioctl(fd, cmd, arg)
    except IOError as ex:
        result = ex.errno
    return result


def open_(name, mode):
    res = -1
    try:
        res = os.open(name, mode)
    except Exception as ex:
        pass
    return res


TMK_VERSION_MIN = 0x0403
TMK_VERSION = 0x0406
TMKUSB_VERSION_MIN = 0x0107

MAX_TMKUSB_NUMBER = 8 - 1
MIN_TMK_TYPE = 2
MAX_TMK_TYPE = 12

TMK400 = 2
TMKMPC = 3
RTMK400 = 4
TMKX = 5
TMKXI = 6
MRTX = 7
MRTXI = 8
TA = 9
TAI = 10
MRTA = 11
MRTAI = 12

ALL_TMKS = 0x00FF

GET_TIMEOUT = 0xFFFF

SWTIMER_OFF = 0x0000
SWTIMER_ON = 0x2400
SWTIMER_EVENT = 0x8000
SWTIMER_RESET = 0xFBFF

GET_SWTIMER_CTRL = 0xFFFF

TIMER_RESET = 0xFBFF
TIMER_OFF = 0x0000
TIMER_16BIT = 0x3400
TIMER_32BIT = 0x2400
TIMER_1US = 0x0000
TIMER_2US = 0x0080
TIMER_4US = 0x0100
TIMER_8US = 0x0180
TIMER_16US = 0x0200
TIMER_32US = 0x0280
TIMER_64US = 0x0300
TIMER_STOP = 0x0380
TIMER_SYN = 0x0040
TIMER_SYND = 0x0020
TIMER_SA = 0x001F

TIMER_NOSTOP = 0x2000

TIMER_MASK = 0x37FF
TIMER_STEP = 0x0380
TIMER_BITS = 0x3400

GET_TIMER_CTRL = 0xFFFF

BUS_A = 0
BUS_B = 1
BUS_1 = 0
BUS_2 = 1

NWORDS_MASK = 0x001F
CMD_MASK = 0x001F
SUBADDR_MASK = 0x03E0
CI_MASK = 0x03E0
HBIT_MASK = 0x0200
RT_DIR_MASK = 0x0400
ADDRESS_MASK = 0xF800
RTFL_MASK = 0x0001
DNBA_MASK = 0x0002
SSFL_MASK = 0x0004
BUSY_MASK = 0x0008
BRCST_MASK = 0x0010
NULL_MASK = 0x00E0
SREQ_MASK = 0x0100
ERROR_MASK = 0x0400

SREQ = 0x01
BUSY = 0x02
SSFL = 0x04
RTFL = 0x08
DNBA = 0x10

CWB0 = 0x20

CWB1 = 0x40

BC_MODE = 0x00
RT_MODE = 0x80
MT_MODE = 0x100
MRT_MODE = 0x280
UNDEFINED_MODE = 0xFFFF

RT_FLAG = 0x8000
RT_FLAG_MASK = 0x8000

CX_CC_MASK = 0x000F
CX_CONT_MASK = 0x0010
CX_BUS_MASK = 0x0020
CX_SIG_MASK = 0x8000
CX_INT_MASK = 0x0020

CX_STOP = 0x0000
CX_BUS_0 = 0x0000
CX_BUS_A = 0x0000
CX_BUS_1 = 0x0020
CX_BUS_B = 0x0020

SX_NOERR = 0
SX_MEO = 1
SX_TOA = 2
SX_TOD = 3
SX_ELN = 4
SX_ERAO = 5
SX_ESYN = 6
SX_EBC = 7

SX_ERR_MASK = 0x0007
SX_IB_MASK = 0x0008
SX_G1_MASK = 0x0010
SX_G2_MASK = 0x0020
SX_K2_MASK = 0x0100
SX_K1_MASK = 0x0200
SX_SCC_MASK = 0x3C00
SX_ME_MASK = 0x4000
SX_BUS_MASK = 0x8000

SX_BUS_0 = 0x0000
SX_BUS_A = 0x0000
SX_BUS_1 = 0x8000
SX_BUS_B = 0x8000

GET_IO_DELAY = 0xFFFF

CMD_DYNAMIC_BUS_CONTROL = 0x400
CMD_SYNCHRONIZE = 0x401
CMD_TRANSMIT_STATUS_WORD = 0x402
CMD_INITIATE_SELF_TEST = 0x403
CMD_TRANSMITTER_SHUTDOWN = 0x404
CMD_OVERRIDE_TRANSMITTER_SHUTDOWN = 0x405
CMD_INHIBIT_TERMINAL_FLAG_BIT = 0x406
CMD_OVERRIDE_INHIBIT_TERMINAL_FLAG_BIT = 0x407
CMD_RESET_REMOTE_TERMINAL = 0x408
CMD_TRANSMIT_VECTOR_WORD = 0x410
CMD_SYNCHRONIZE_WITH_DATA_WORD = 0x011
CMD_TRANSMIT_LAST_COMMAND_WORD = 0x412
CMD_TRANSMIT_BUILT_IN_TEST_WORD = 0x413

TMK_BAD_0 = -1024
TMK_BAD_TYPE = (TMK_BAD_0 - 1)
TMK_BAD_IRQ = (TMK_BAD_0 - 2)
TMK_BAD_NUMBER = (TMK_BAD_0 - 3)
BC_BAD_BUS = (TMK_BAD_0 - 4)
BC_BAD_BASE = (TMK_BAD_0 - 5)
BC_BAD_LEN = (TMK_BAD_0 - 6)
RT_BAD_PAGE = (TMK_BAD_0 - 7)
RT_BAD_LEN = (TMK_BAD_0 - 8)
RT_BAD_ADDRESS = (TMK_BAD_0 - 9)
RT_BAD_FUNC = (TMK_BAD_0 - 10)
BC_BAD_FUNC = (TMK_BAD_0 - 11)
TMK_BAD_FUNC = (TMK_BAD_0 - 12)
VTMK_BAD_VERSION = (TMK_BAD_0 - 13)

TMK_IOC_MAGIC = ord('k')
TMK_IOC0 = 0

VTMK_tmkconfig = 2
VTMK_tmkdone = 3
VTMK_tmkgetmaxn = 4
VTMK_tmkselect = 5
VTMK_tmkselected = 6
VTMK_tmkgetmode = 7
VTMK_tmksetcwbits = 8
VTMK_tmkclrcwbits = 9
VTMK_tmkgetcwbits = 10
VTMK_tmkwaitevents = 11

VTMK_tmkgetevd = 12

VTMK_bcreset = 13
VTMK_bc_def_tldw = 14
VTMK_bc_enable_di = 15
VTMK_bc_disable_di = 16
VTMK_bcdefirqmode = 17
VTMK_bcgetirqmode = 18
VTMK_bcgetmaxbase = 19
VTMK_bcdefbase = 20
VTMK_bcgetbase = 21
VTMK_bcputw = 22
VTMK_bcgetw = 23
VTMK_bcgetansw = 24
VTMK_bcputblk = 25
VTMK_bcgetblk = 26
VTMK_bcdefbus = 27
VTMK_bcgetbus = 28
VTMK_bcstart = 29
VTMK_bcstartx = 30
VTMK_bcdeflink = 31
VTMK_bcgetlink = 32
VTMK_bcstop = 33
VTMK_bcgetstate = 34

VTMK_rtreset = 35
VTMK_rtdefirqmode = 36
VTMK_rtgetirqmode = 37
VTMK_rtdefmode = 38
VTMK_rtgetmode = 39
VTMK_rtgetmaxpage = 40
VTMK_rtdefpage = 41
VTMK_rtgetpage = 42
VTMK_rtdefpagepc = 43
VTMK_rtdefpagebus = 44
VTMK_rtgetpagepc = 45
VTMK_rtgetpagebus = 46
VTMK_rtdefaddress = 47
VTMK_rtgetaddress = 48
VTMK_rtdefsubaddr = 49
VTMK_rtgetsubaddr = 50
VTMK_rtputw = 51
VTMK_rtgetw = 52
VTMK_rtputblk = 53
VTMK_rtgetblk = 54
VTMK_rtsetanswbits = 55
VTMK_rtclranswbits = 56
VTMK_rtgetanswbits = 57
VTMK_rtgetflags = 58
VTMK_rtputflags = 59
VTMK_rtsetflag = 60
VTMK_rtclrflag = 61
VTMK_rtgetflag = 62
VTMK_rtgetstate = 63
VTMK_rtbusy = 64
VTMK_rtlock = 65
VTMK_rtunlock = 66
VTMK_rtgetcmddata = 67
VTMK_rtputcmddata = 68

VTMK_mtreset = 69
VTMK_mtdefirqmode = 70
VTMK_mtgetirqmode = 71
VTMK_mtgetmaxbase = 72
VTMK_mtdefbase = 73
VTMK_mtgetbase = 74
VTMK_mtputw = 75
VTMK_mtgetw = 76
VTMK_mtgetsw = 77
VTMK_mtputblk = 78
VTMK_mtgetblk = 79
VTMK_mtstartx = 80
VTMK_mtdeflink = 81
VTMK_mtgetlink = 82
VTMK_mtstop = 83
VTMK_mtgetstate = 84

VTMK_tmkgetinfo = 85
VTMK_GetVersion = 86

VTMK_rtenable = 87

VTMK_mrtgetmaxn = 88
VTMK_mrtconfig = 89
VTMK_mrtselected = 90
VTMK_mrtgetstate = 91
VTMK_mrtdefbrcsubaddr0 = 92
VTMK_mrtreset = 93

VTMK_tmktimer = 94
VTMK_tmkgettimer = 95
VTMK_tmkgettimerl = 96
VTMK_bcgetmsgtime = 97
VTMK_mtgetmsgtime = 98
VTMK_rtgetmsgtime = 99

VTMK_tmkgethwver = 100

VTMK_tmkgetevtime = 101
VTMK_tmkswtimer = 102
VTMK_tmkgetswtimer = 103

VTMK_tmktimeout = 104

VTMK_mrtdefbrcpage = 105
VTMK_mrtgetbrcpage = 106

TMK_IOC_MAXNR = 106
TMK_IOCGetVersion = ioctl._IO(TMK_IOC_MAGIC, VTMK_GetVersion + TMK_IOC0)
TMK_IOCmrtdefbrcpage = ioctl._IO(TMK_IOC_MAGIC, VTMK_mrtdefbrcpage + TMK_IOC0)

VTMK_tmkwaiteventsflag = 115

_hVTMK4VxD = 0

TMK_IOCtmkconfig = ioctl._IO(TMK_IOC_MAGIC, VTMK_tmkconfig + TMK_IOC0)
TMK_IOCtmkdone = ioctl._IO(TMK_IOC_MAGIC, VTMK_tmkdone + TMK_IOC0)
TMK_IOCtmkgetmaxn = ioctl._IO(TMK_IOC_MAGIC, VTMK_tmkgetmaxn + TMK_IOC0)
TMK_IOCtmkselect = ioctl._IO(TMK_IOC_MAGIC, VTMK_tmkselect + TMK_IOC0)
TMK_IOCtmkselected = ioctl._IO(TMK_IOC_MAGIC, VTMK_tmkselected + TMK_IOC0)
TMK_IOCtmkgetmode = ioctl._IO(TMK_IOC_MAGIC, VTMK_tmkgetmode + TMK_IOC0)
TMK_IOCtmksetcwbits = ioctl._IO(TMK_IOC_MAGIC, VTMK_tmksetcwbits + TMK_IOC0)
TMK_IOCtmkclrcwbits = ioctl._IO(TMK_IOC_MAGIC, VTMK_tmkclrcwbits + TMK_IOC0)
TMK_IOCtmkgetcwbits = ioctl._IO(TMK_IOC_MAGIC, VTMK_tmkgetcwbits + TMK_IOC0)
TMK_IOCtmkwaitevents = ioctl._IOW(TMK_IOC_MAGIC, VTMK_tmkwaitevents + TMK_IOC0, 8)

TMK_IOCtmkgetevd = ioctl._IOR(TMK_IOC_MAGIC, VTMK_tmkgetevd + TMK_IOC0, 22)

TMK_IOCbcreset = ioctl._IO(TMK_IOC_MAGIC, VTMK_bcreset + TMK_IOC0)

TMK_IOCbcdefirqmode = ioctl._IO(TMK_IOC_MAGIC, VTMK_bcdefirqmode + TMK_IOC0)
TMK_IOCbcgetirqmode = ioctl._IO(TMK_IOC_MAGIC, VTMK_bcgetirqmode + TMK_IOC0)
TMK_IOCbcgetmaxbase = ioctl._IO(TMK_IOC_MAGIC, VTMK_bcgetmaxbase + TMK_IOC0)
TMK_IOCbcdefbase = ioctl._IO(TMK_IOC_MAGIC, VTMK_bcdefbase + TMK_IOC0)
TMK_IOCbcgetbase = ioctl._IO(TMK_IOC_MAGIC, VTMK_bcgetbase + TMK_IOC0)
TMK_IOCbcputw = ioctl._IO(TMK_IOC_MAGIC, VTMK_bcputw + TMK_IOC0)
TMK_IOCbcgetw = ioctl._IO(TMK_IOC_MAGIC, VTMK_bcgetw + TMK_IOC0)
TMK_IOCbcgetansw = ioctl._IOWR(TMK_IOC_MAGIC, VTMK_bcgetansw + TMK_IOC0, 4)
TMK_IOCbcputblk = ioctl._IOW(TMK_IOC_MAGIC, VTMK_bcputblk + TMK_IOC0, 16)
TMK_IOCbcgetblk = ioctl._IOW(TMK_IOC_MAGIC, VTMK_bcgetblk + TMK_IOC0, 16)
TMK_IOCbcdefbus = ioctl._IO(TMK_IOC_MAGIC, VTMK_bcdefbus + TMK_IOC0)
TMK_IOCbcgetbus = ioctl._IO(TMK_IOC_MAGIC, VTMK_bcgetbus + TMK_IOC0)
TMK_IOCbcstart = ioctl._IO(TMK_IOC_MAGIC, VTMK_bcstart + TMK_IOC0)
TMK_IOCbcstartx = ioctl._IO(TMK_IOC_MAGIC, VTMK_bcstartx + TMK_IOC0)
TMK_IOCbcdeflink = ioctl._IO(TMK_IOC_MAGIC, VTMK_bcdeflink + TMK_IOC0)
TMK_IOCbcgetlink = ioctl._IOR(TMK_IOC_MAGIC, VTMK_bcgetlink + TMK_IOC0, 4)
TMK_IOCbcstop = ioctl._IO(TMK_IOC_MAGIC, VTMK_bcstop + TMK_IOC0)
TMK_IOCbcgetstate = ioctl._IOR(TMK_IOC_MAGIC, VTMK_bcgetstate + TMK_IOC0, 4)

TMK_IOCrtreset = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtreset + TMK_IOC0)
TMK_IOCrtdefirqmode = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtdefirqmode + TMK_IOC0)
TMK_IOCrtgetirqmode = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtgetirqmode + TMK_IOC0)
TMK_IOCrtdefmode = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtdefmode + TMK_IOC0)
TMK_IOCrtgetmode = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtgetmode + TMK_IOC0)
TMK_IOCrtgetmaxpage = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtgetmaxpage + TMK_IOC0)
TMK_IOCrtdefpage = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtdefpage + TMK_IOC0)
TMK_IOCrtgetpage = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtgetpage + TMK_IOC0)
TMK_IOCrtdefpagepc = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtdefpagepc + TMK_IOC0)
TMK_IOCrtdefpagebus = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtdefpagebus + TMK_IOC0)
TMK_IOCrtgetpagepc = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtgetpagepc + TMK_IOC0)
TMK_IOCrtgetpagebus = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtgetpagebus + TMK_IOC0)
TMK_IOCrtdefaddress = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtdefaddress + TMK_IOC0)
TMK_IOCrtgetaddress = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtgetaddress + TMK_IOC0)
TMK_IOCrtdefsubaddr = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtdefsubaddr + TMK_IOC0)
TMK_IOCrtgetsubaddr = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtgetsubaddr + TMK_IOC0)
TMK_IOCrtputw = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtputw + TMK_IOC0)
TMK_IOCrtgetw = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtgetw + TMK_IOC0)
TMK_IOCrtputblk = ioctl._IOW(TMK_IOC_MAGIC, VTMK_rtputblk + TMK_IOC0, 16)
TMK_IOCrtgetblk = ioctl._IOW(TMK_IOC_MAGIC, VTMK_rtgetblk + TMK_IOC0, 16)
TMK_IOCrtsetanswbits = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtsetanswbits + TMK_IOC0)
TMK_IOCrtclranswbits = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtclranswbits + TMK_IOC0)
TMK_IOCrtgetanswbits = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtgetanswbits + TMK_IOC0)
TMK_IOCrtgetflags = ioctl._IOW(TMK_IOC_MAGIC, VTMK_rtgetflags + TMK_IOC0, 16)
TMK_IOCrtputflags = ioctl._IOW(TMK_IOC_MAGIC, VTMK_rtputflags + TMK_IOC0, 16)
TMK_IOCrtsetflag = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtsetflag + TMK_IOC0)
TMK_IOCrtclrflag = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtclrflag + TMK_IOC0)
TMK_IOCrtgetflag = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtgetflag + TMK_IOC0)
TMK_IOCrtgetstate = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtgetstate + TMK_IOC0)
TMK_IOCrtbusy = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtbusy + TMK_IOC0)
TMK_IOCrtlock = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtlock + TMK_IOC0)
TMK_IOCrtunlock = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtunlock + TMK_IOC0)
TMK_IOCrtgetcmddata = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtgetcmddata + TMK_IOC0)
TMK_IOCrtputcmddata = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtputcmddata + TMK_IOC0)

TMK_IOCmtreset = ioctl._IO(TMK_IOC_MAGIC, VTMK_mtreset + TMK_IOC0)
TMK_IOCmtdefirqmode = ioctl._IO(TMK_IOC_MAGIC, VTMK_mtdefirqmode + TMK_IOC0)
TMK_IOCmtgetirqmode = ioctl._IO(TMK_IOC_MAGIC, VTMK_mtgetirqmode + TMK_IOC0)
TMK_IOCmtgetmaxbase = ioctl._IO(TMK_IOC_MAGIC, VTMK_mtgetmaxbase + TMK_IOC0)
TMK_IOCmtdefbase = ioctl._IO(TMK_IOC_MAGIC, VTMK_mtdefbase + TMK_IOC0)
TMK_IOCmtgetbase = ioctl._IO(TMK_IOC_MAGIC, VTMK_mtgetbase + TMK_IOC0)
TMK_IOCmtputw = ioctl._IO(TMK_IOC_MAGIC, VTMK_mtputw + TMK_IOC0)
TMK_IOCmtgetw = ioctl._IO(TMK_IOC_MAGIC, VTMK_mtgetw + TMK_IOC0)
TMK_IOCmtgetsw = ioctl._IO(TMK_IOC_MAGIC, VTMK_mtgetsw + TMK_IOC0)
TMK_IOCmtputblk = ioctl._IOW(TMK_IOC_MAGIC, VTMK_mtputblk + TMK_IOC0, 16)
TMK_IOCmtgetblk = ioctl._IOW(TMK_IOC_MAGIC, VTMK_mtgetblk + TMK_IOC0, 16)
TMK_IOCmtstartx = ioctl._IO(TMK_IOC_MAGIC, VTMK_mtstartx + TMK_IOC0)
TMK_IOCmtdeflink = ioctl._IO(TMK_IOC_MAGIC, VTMK_mtdeflink + TMK_IOC0)
TMK_IOCmtgetlink = ioctl._IOR(TMK_IOC_MAGIC, VTMK_mtgetlink + TMK_IOC0, 4)
TMK_IOCmtstop = ioctl._IO(TMK_IOC_MAGIC, VTMK_mtstop + TMK_IOC0)
TMK_IOCmtgetstate = ioctl._IOR(TMK_IOC_MAGIC, VTMK_mtgetstate + TMK_IOC0, 4)

TMK_IOCtmkgetinfo = ioctl._IOR(TMK_IOC_MAGIC, VTMK_tmkgetinfo + TMK_IOC0, 22)

TMK_IOCrtenable = ioctl._IO(TMK_IOC_MAGIC, VTMK_rtenable + TMK_IOC0)

TMK_IOCmrtgetmaxn = ioctl._IO(TMK_IOC_MAGIC, VTMK_mrtgetmaxn + TMK_IOC0)
TMK_IOCmrtconfig = ioctl._IO(TMK_IOC_MAGIC, VTMK_mrtconfig + TMK_IOC0)
TMK_IOCmrtselected = ioctl._IO(TMK_IOC_MAGIC, VTMK_mrtselected + TMK_IOC0)
TMK_IOCmrtgetstate = ioctl._IO(TMK_IOC_MAGIC, VTMK_mrtgetstate + TMK_IOC0)
TMK_IOCmrtdefbrcsubaddr0 = ioctl._IO(TMK_IOC_MAGIC, VTMK_mrtdefbrcsubaddr0 + TMK_IOC0)
TMK_IOCmrtreset = ioctl._IO(TMK_IOC_MAGIC, VTMK_mrtreset + TMK_IOC0)

TMK_IOCtmktimer = ioctl._IO(TMK_IOC_MAGIC, VTMK_tmktimer + TMK_IOC0)
TMK_IOCtmkgettimer = ioctl._IOR(TMK_IOC_MAGIC, VTMK_tmkgettimer + TMK_IOC0, 4)
TMK_IOCtmkgettimerl = ioctl._IO(TMK_IOC_MAGIC, VTMK_tmkgettimerl + TMK_IOC0)
TMK_IOCbcgetmsgtime = ioctl._IOR(TMK_IOC_MAGIC, VTMK_bcgetmsgtime + TMK_IOC0, 4)
TMK_IOCmtgetmsgtime = ioctl._IOR(TMK_IOC_MAGIC, VTMK_mtgetmsgtime + TMK_IOC0, 4)
TMK_IOCrtgetmsgtime = ioctl._IOR(TMK_IOC_MAGIC, VTMK_rtgetmsgtime + TMK_IOC0, 4)

TMK_IOCtmkgethwver = ioctl._IO(TMK_IOC_MAGIC, VTMK_tmkgethwver + TMK_IOC0)

TMK_IOCtmkgetevtime = ioctl._IOR(TMK_IOC_MAGIC, VTMK_tmkgetevtime + TMK_IOC0, 4)
TMK_IOCtmkswtimer = ioctl._IO(TMK_IOC_MAGIC, VTMK_tmkswtimer + TMK_IOC0)
TMK_IOCtmkgetswtimer = ioctl._IOR(TMK_IOC_MAGIC, VTMK_tmkgetswtimer + TMK_IOC0, 4)

TMK_IOCtmktimeout = ioctl._IO(TMK_IOC_MAGIC, VTMK_tmktimeout + TMK_IOC0)

TMK_IOCmrtgetbrcpage = ioctl._IO(TMK_IOC_MAGIC, VTMK_mrtgetbrcpage + TMK_IOC0)

TMK_IOCtmkwaiteventsflag = ioctl._IOW(TMK_IOC_MAGIC, VTMK_tmkwaiteventsflag + TMK_IOC0, 16)


class Mil1553LinuxDriver:

    @staticmethod
    def CW(ADDR, DIR, SUBADDR, NWORDS):
        return (ADDR << 11) | DIR | (SUBADDR << 5) | (NWORDS & 0x1F)

    @staticmethod
    def CWM(ADDR, COMMAND):
        return (ADDR << 11) | CI_MASK | COMMAND

    @staticmethod
    def CWMC(ADDR, CI, COMMAND):
        return (ADDR << 11) | (CI & 0x03E0) | COMMAND

    def __init__(self):
        self.tmkUsbCnt = 0
        self.tmkCnt = 0
        self.tmkCurNumber = -1
        self.tmkUsbNumMap = [0 for _ in range(MAX_TMKUSB_NUMBER + 1)]
        self._ahVTMK4VxDusb = [0 for _ in range(MAX_TMKUSB_NUMBER + 1)]

    def rtbusy(self):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCrtbusy,0)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtbusy)

    def rtgetcmddata(self, rtBusCommand):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCrtgetcmddata, rtBusCommand)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtgetcmddata, rtBusCommand)

    def rtenable(self, rtEnable):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCrtenable, rtEnable)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtenable, rtEnable)

    def tmk_open(self):
        global _hVTMK4VxD
        _VTMK4Arg = 0
        if _hVTMK4VxD != 0:
            return 0
        self.tmkCnt = 0
        _hVTMK4VxD = open_("/dev/tmk1553b", 0)
        if _hVTMK4VxD < 0:
            _hVTMK4VxD = 0
        _VTMK4Arg = ioctl_(_hVTMK4VxD, TMK_IOCGetVersion, 0)
        if (_VTMK4Arg < 0) or (_VTMK4Arg < TMK_VERSION_MIN):
            os.close(Mil1553LinuxDriver._hVTMK4VxD)
            Mil1553LinuxDriver._hVTMK4VxD = 0
            return VTMK_BAD_VERSION
        else:
            self.tmkCnt = ioctl_(_hVTMK4VxD, TMK_IOCtmkgetmaxn,0) + 1

        self.tmkUsbCnt = 0
        for iTMK in range(MAX_TMKUSB_NUMBER):
            self._ahVTMK4VxDusb[iTMK] = 0
            self.tmkUsbNumMap[iTMK] = 0

        for iTMK in range(MAX_TMKUSB_NUMBER):
            devName = "/dev/tmk1553busb%d" % iTMK
            self._ahVTMK4VxDusb[self.tmkUsbCnt] = open_(devName, 0)
            if self._ahVTMK4VxDusb[self.tmkUsbCnt] < 0:
                self._ahVTMK4VxDusb[self.tmkUsbCnt] = 0
                continue
            _VTMK4Arg = ioctl_(self._ahVTMK4VxDusb[self.tmkUsbCnt], TMK_IOCGetVersion, 0)
            if _VTMK4Arg < 0 or _VTMK4Arg < TMKUSB_VERSION_MIN:
                os.close(self._ahVTMK4VxDusb[self.tmkUsbCnt])
                self._ahVTMK4VxDusb[self.tmkUsbCnt] = 0
                return VTMK_BAD_VERSION
            else:
                os.close(self._ahVTMK4VxDusb[self.tmkUsbCnt])
                self._ahVTMK4VxDusb[self.tmkUsbCnt] = 0
            self.tmkUsbNumMap[self.tmkUsbCnt] = iTMK
            self.tmkUsbCnt += 1

        if not (_hVTMK4VxD == 0) and not (self.tmkUsbCnt == 0):
            return -1
        return 0

    def mtgetsw(self):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCmtgetsw,0)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCmtgetsw)

    def tmkconfig(self, tmkNumber):
        if tmkNumber < 0 or tmkNumber >= self.tmkCnt + self.tmkUsbCnt:
            return TMK_BAD_NUMBER
        if tmkNumber < self.tmkCnt:
            if _hVTMK4VxD == 0:
                return TMK_BAD_NUMBER
            self.tmkCurNumber = tmkNumber
            return ioctl_(_hVTMK4VxD, TMK_IOCtmkconfig, tmkNumber)

        devName = "/dev/tmk1553busb%d" % self.tmkUsbNumMap[tmkNumber - self.tmkCnt]
        self._ahVTMK4VxDusb[tmkNumber - self.tmkCnt] = os.open(devName, 0)
        if self._ahVTMK4VxDusb[tmkNumber - self.tmkCnt] == 0 or self._ahVTMK4VxDusb[tmkNumber - self.tmkCnt] < 0:
            self._ahVTMK4VxDusb[tmkNumber - self.tmkCnt] = 0
            return TMK_BAD_NUMBER

        Result = ioctl_(self._ahVTMK4VxDusb[tmkNumber - self.tmkCnt], TMK_IOCtmkconfig, tmkNumber)
        if Result == 0:
            self.tmkCurNumber = tmkNumber
        return Result

    def tmkgetmaxn(self):
        if _hVTMK4VxD != 0:
            return ioctl_(_hVTMK4VxD, TMK_IOCtmkgetmaxn) + self.tmkUsbCnt
        else:
            return self.tmkUsbCnt - 1

    def tmkdone(self, tmkNumber):
        # int iTMK, bTMK, eTMK
        Result = 0
        if tmkNumber < self.tmkCnt and tmkNumber != ALL_TMKS:
            if _hVTMK4VxD == 0:
                return TMK_BAD_NUMBER
            self.tmkCurNumber = -1
            return ioctl_(_hVTMK4VxD, TMK_IOCtmkdone, tmkNumber)

        if tmkNumber == ALL_TMKS:
            self.tmkCurNumber = -1
            ioctl_(_hVTMK4VxD, TMK_IOCtmkdone, tmkNumber)
            bTMK = 0
            eTMK = self.tmkUsbCnt - 1
        elif tmkNumber < 0 or tmkNumber >= self.tmkCnt + self.tmkUsbCnt:
            return TMK_BAD_NUMBER
        else:
            if tmkNumber == self.tmkCurNumber:
                self.tmkCurNumber = -1
            bTMK = eTMK = tmkNumber - self.tmkCnt

        for iTMK in range(bTMK, eTMK, 1):
            if self._ahVTMK4VxDusb[iTMK] == 0:
                Result = ioctl_(self._ahVTMK4VxDusb[iTMK], TMK_IOCtmkdone, iTMK)
                os.close(self._ahVTMK4VxDusb[iTMK])

            self._ahVTMK4VxDusb[iTMK] = 0

        return Result

    def tmkselect(self, tmkNumber):
        if tmkNumber < 0 or tmkNumber >= self.tmkCnt + self.tmkUsbCnt:
            return TMK_BAD_NUMBER
        if tmkNumber < self.tmkCnt:
            if _hVTMK4VxD == 0:
                return TMK_BAD_NUMBER
            self.tmkCurNumber = tmkNumber
            return ioctl_(_hVTMK4VxD, TMK_IOCtmkselect, tmkNumber)

        if self._ahVTMK4VxDusb[tmkNumber - self.tmkCnt] == 1:
            self.tmkCurNumber = tmkNumber
        else:
            self.tmkCurNumber = -1
            return TMK_BAD_NUMBER

        return 0

    def tmkselected(self):
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCtmkselected)
        else:
            return self.tmkCurNumber

    def tmkgetmode(self):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCtmkgetmode)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCtmkgetmode)

    def tmksetcwbits(self, tmkSetControl):
        if self.tmkCurNumber < 0:
            return
        if self.tmkCurNumber < self.tmkCnt:
            ioctl_(_hVTMK4VxD, TMK_IOCtmksetcwbits, tmkSetControl)
            return
        ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCtmksetcwbits, tmkSetControl)

    def tmkclrcwbits(self, tmkClrControl):
        if self.tmkCurNumber < 0:
            return
        if self.tmkCurNumber < self.tmkCnt:
            ioctl_(_hVTMK4VxD, TMK_IOCtmksetcwbits, tmkClrControl)
            return

        ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCtmksetcwbits, tmkClrControl)

    def tmkgetcwbits(self):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCtmkgetcwbits)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCtmkgetcwbits)

    def tmkwaitevents(self, maskEvents, fWait):
        class Arg(ctypes.Structure):
            _fields_=[("arg",ctypes.c_uint32*2)]
        _VTMK4Arg = Arg()
        tmkMask = 0
        DrvMask = 0

        if self.tmkCnt > 31:
            DevMask = 0xFFFFFFFF
        else:
            DevMask = (1 << self.tmkCnt) - 1
        if (maskEvents & DevMask) == 0:  # // usb only
            _VTMK4Arg.arg[0] = 0
            _VTMK4Arg.arg[1] = fWait
            for iTMK in range(self.tmkUsbCnt):
                if (maskEvents != 0 & (1 << (iTMK + self.tmkCnt)) != 0) and self._ahVTMK4VxDusb[iTMK] != 0:
                    _VTMK4Arg[0] |= 1 << self.tmkUsbNumMap[iTMK]

            if _VTMK4Arg[0] != 0:
                for iTMK in range(self.tmkUsbCnt):
                    if self._ahVTMK4VxDusb[iTMK] != 0:
                        DrvMask = ioctl_(self._ahVTMK4VxDusb[iTMK], TMK_IOCtmkwaitevents, _VTMK4Arg)
                        break

                if DrvMask > 0:
                    for iTMK in range(self.tmkUsbCnt):
                        if DrvMask != 0 & (1 << self.tmkUsbNumMap[iTMK]) != 0:
                            tmkMask |= 1 << (iTMK + self.tmkCnt)

                else:
                    return DrvMask

            return tmkMask
        elif (maskEvents >> self.tmkCnt) == 0:  # // tmk only
            _VTMK4Arg.arg[0] = maskEvents
            _VTMK4Arg.arg[1] = fWait
            if _hVTMK4VxD != 0 and _VTMK4Arg.arg[0] != 0:
                tmkMask = ioctl_(_hVTMK4VxD, TMK_IOCtmkwaitevents, _VTMK4Arg)
            return tmkMask
        else:
            print("Else")
        return tmkMask

    def tmkgetevd(self, pEvD):
        if self.tmkCurNumber < 0:
            return
        elif self.tmkCurNumber < self.tmkCnt:
            ioctl_(_hVTMK4VxD, TMK_IOCtmkgetevd, pEvD)
        else:
            ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCtmkgetevd, pEvD)





    def tmkgetinfo(self, pConfD):
        if self.tmkCurNumber < 0:
            return
        if self.tmkCurNumber < self.tmkCnt:
            fcntl.ioctl(_hVTMK4VxD, TMK_IOCtmkgetinfo, pConfD)
            return
        fcntl.ioctl(_hVTMK4VxD, TMK_IOCtmkgetinfo, pConfD)

    def bcreset(self):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCbcreset,0)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCbcreset)

    def mtreset(self):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCmtreset,0)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCmtreset)

    def mtdefirqmode(self, mtIrqMode):
        return self.bcdefirqmode(mtIrqMode)

    def bcdefirqmode(self, bcIrqMode):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCbcdefirqmode, bcIrqMode)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCbcdefirqmode, bcIrqMode)

    def bcgetirqmode(self):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCbcgetirqmode)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCbcgetirqmode)

    def mtgetmaxbase(self):
        return self.bcgetmaxbase()

    def bcgetmaxbase(self):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCbcgetmaxbase,0)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCbcgetmaxbase)

    def mtdefbase(self, mtBasePC):
        return self.bcdefbase(mtBasePC)

    def bcdefbase(self, bcBasePC):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCbcdefbase, bcBasePC)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCbcdefbase & 0xffffffff, bcBasePC)

    def bcgetbase(self):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCbcgetbase)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCbcgetbase)

    def bcputw(self, bcAddr, bcData):
        if self.tmkCurNumber < 0:
            return
        if self.tmkCurNumber < self.tmkCnt:
            ioctl_(_hVTMK4VxD, TMK_IOCbcputw, bcAddr | (bcData << 16))
            return
        ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCbcputw, bcAddr | (bcData << 16))

    def bcgetw(self, bcAddr):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCbcgetw, bcAddr)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCbcgetw, bcAddr)

    def bcgetansw(self, bcCtrlCode):
        _VTMK4Arg = bcCtrlCode
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            ioctl_(_hVTMK4VxD, TMK_IOCbcgetansw, _VTMK4Arg)
            return _VTMK4Arg
        ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCbcgetansw, _VTMK4Arg)
        return _VTMK4Arg

    def rtgetblk(self, rtAddr, pcBuffer, cwLength):
        c = (ctypes.c_void_p * 2)()
        c[0] = rtAddr | cwLength << 16
        c[1] = ctypes.addressof(pcBuffer)
        if self.tmkCurNumber < 0:
            return
        if self.tmkCurNumber < self.tmkCnt:
            ioctl_(_hVTMK4VxD, TMK_IOCrtgetblk, c)
            return
        ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtgetblk, c)

    def rtputcmddata(self, rtBusCommand, rtData):
        if self.tmkCurNumber < 0:
            return
        if self.tmkCurNumber < self.tmkCnt:
            ioctl_(_hVTMK4VxD, TMK_IOCrtputcmddata, rtBusCommand | (rtData << 16))
            return
        ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtputcmddata, rtBusCommand | (rtData << 16))

    def rtputblk(self, rtAddr, pcBuffer, cwLength):
        c = (ctypes.c_void_p * 2)()
        c[0] = rtAddr | cwLength << 16
        c[1] = ctypes.addressof(pcBuffer)
        if self.tmkCurNumber < 0:
            return
        if self.tmkCurNumber < self.tmkCnt:
            ioctl_(_hVTMK4VxD, TMK_IOCrtputblk, c)
            return
        ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtputblk, c)

    def bcputblk(self, bcAddr, pcBuffer, cwLength):
        c = (ctypes.c_void_p * 2)()
        c[0] = bcAddr | cwLength << 16
        c[1] = ctypes.addressof(pcBuffer)
        if self.tmkCurNumber < 0:
            return
        if self.tmkCurNumber < self.tmkCnt:
            ioctl_(_hVTMK4VxD, TMK_IOCbcputblk, c)
            return
        ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCbcputblk, c)

    def mtgetblk(self, mtAddr, pcBuffer, cwLength):
        self.bcgetblk(mtAddr, pcBuffer, cwLength)

    def bcgetblk(self, bcAddr, pcBuffer, cwLength):
        c = (ctypes.c_void_p * 2)()
        c[0] = bcAddr | cwLength << 16
        c[1] = ctypes.addressof(pcBuffer)
        if self.tmkCurNumber < 0:
            return
        if self.tmkCurNumber < self.tmkCnt:
            ioctl_(_hVTMK4VxD, TMK_IOCbcgetblk, c)
            return

        ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCbcgetblk, c)

    def bcdefbus(self, bcBus):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCbcdefbus, bcBus)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCbcdefbus, bcBus)

    def bcgetbus(self):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCbcgetbus)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCbcgetbus)

    def bcstart(self, bcBase, bcCtrlCode):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCbcstart, bcBase | (bcCtrlCode << 16))
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCbcstart, bcBase | (bcCtrlCode << 16))

    def mtstartx(self, mtBase, mtCtrlCode):
        return self.bcstartx(mtBase, mtCtrlCode)

    def bcstartx(self, bcBase, bcCtrlCode):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCbcstartx, bcBase | (bcCtrlCode << 16))
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCbcstartx,
                      bcBase | (bcCtrlCode << 16))

    def mtdeflink(self, mtBase, mtCtrlCode):
        return self.bcdeflink(mtBase, mtCtrlCode)

    def bcdeflink(self, bcBase, bcCtrlCode):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctrext(_hVTMK4VxD, TMK_IOCbcdeflink, bcBase | (bcCtrlCode << 16))
        return ioctrext(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCbcdeflink,
                      bcBase | (bcCtrlCode << 16))

    def bcgetlink(self):
        # class C extends Structure {
        #    int _VTMK4Arg;
        # }
        # C c = new C()
        c = ctypes.c_uint32()
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            ioctl_(_hVTMK4VxD, TMK_IOCbcgetlink, c)
            return c

        ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCbcgetlink, c)
        return c

    def mtstop(self):
        return self.bcstop()

    def bcstop(self):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCbcstop,0)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCbcstop)

    def bcgetstate(self):
        c = ctypes.c_uint32()
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            ioctl_(_hVTMK4VxD, TMK_IOCbcgetstate, c)
            return c.value

        ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCbcgetstate, c)
        return c.value

    def rtreset(self):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCrtreset,0)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtreset)

    def rtdefirqmode(self, rtIrqMode):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCrtdefirqmode, rtIrqMode)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtdefirqmode, rtIrqMode)

    def rtgetirqmode(self):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCrtgetirqmode)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtgetirqmode)

    def rtdefmode(self, rtMode):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCrtdefmode, rtMode)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtdefmode, rtMode)

    def rtgetmode(self):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCrtgetmode)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtgetmode)

    def rtgetmaxpage(self):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCrtgetmaxpage)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtgetmaxpage)

    def rtdefpage(self, rtPage):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCrtdefpage, rtPage)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtdefpage, rtPage)

    def rtgetpage(self):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCrtgetpage)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtgetpage)

    def rtdefpagepc(self, rtPagePC):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCrtdefpagepc, rtPagePC)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtdefpagepc, rtPagePC)

    def rtdefpagebus(self, rtPageBus):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCrtdefpagebus, rtPageBus)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtdefpagebus, rtPageBus)

    def rtgetpagepc(self):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCrtgetpagepc)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtgetpagepc)

    def rtgetpagebus(self):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCrtgetpagebus)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtgetpagebus)

    def rtdefaddress(self, rtAddress):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCrtdefaddress, rtAddress)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtdefaddress, rtAddress)

    def rtgetaddress(self):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCrtgetaddress)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtgetaddress)

    def rtdefsubaddr(self, rtDir, rtSubAddr):
        if self.tmkCurNumber < 0:
            return
        if self.tmkCurNumber < self.tmkCnt:
            ioctl_(_hVTMK4VxD, TMK_IOCrtdefsubaddr, rtDir | (rtSubAddr << 16))
            return
        ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtdefsubaddr, rtDir | (rtSubAddr << 16))

    def rtgetsubaddr(self):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCrtgetsubaddr)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtgetsubaddr)

    def rtputw(self, rtAddr, rtData):
        if self.tmkCurNumber < 0:
            return
        if self.tmkCurNumber < self.tmkCnt:
            ioctl_(_hVTMK4VxD, TMK_IOCrtputw, rtAddr | (rtData << 16))
            return
        ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtputw, rtAddr | (rtData << 16))

    def rtgetw(self, rtAddr):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCrtgetw, rtAddr)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtgetw, rtAddr)

    def rtsetanswbits(self, rtSetControl):
        if self.tmkCurNumber < 0:
            return
        if self.tmkCurNumber < self.tmkCnt:
            ioctl_(_hVTMK4VxD, TMK_IOCrtsetanswbits, rtSetControl)
            return
        ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtsetanswbits, rtSetControl)

    def rtclranswbits(self, rtClrControl):
        if self.tmkCurNumber < 0:
            return
        if self.tmkCurNumber < self.tmkCnt:
            ioctl_(_hVTMK4VxD, TMK_IOCrtclranswbits, rtClrControl)
            return
        ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtclranswbits, rtClrControl)

    def rtgetanswbits(self):
        if self.tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if self.tmkCurNumber < self.tmkCnt:
            return ioctl_(_hVTMK4VxD, TMK_IOCrtgetanswbits,0)
        return ioctl_(self._ahVTMK4VxDusb[self.tmkCurNumber - self.tmkCnt], TMK_IOCrtgetanswbits)
