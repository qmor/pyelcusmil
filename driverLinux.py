from LTMK import ioctl
class Mil1553LinuxDriver:
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
    @staticmethod
    def CW(ADDR,DIR,SUBADDR,NWORDS):
        return (((ADDR) << 11) | (DIR) | ((SUBADDR) << 5) | ((NWORDS) & 0x1F))

    @staticmethod
    def CWM(ADDR, COMMAND):
        return (((ADDR) << 11) | (CI_MASK) | (COMMAND))

    @staticmethod
    def CWMC(ADDR, CI, COMMAND):
        return (((ADDR) << 11) | ((CI) & 0x03E0) | (COMMAND))



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

    tmkUsbCnt = 0
    tmkCnt = 0
    tmkCurNumber = -1
    tmkUsbNumMap = [0 for i in range(MAX_TMKUSB_NUMBER+1)]
    _ahVTMK4VxDusb = [0 for i in range(MAX_TMKUSB_NUMBER + 1)]

    def rtbusy(self):
        if tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if tmkCurNumber < tmkCnt:
            return CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtbusy)
        return CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtbusy)


    def rtgetcmddata(self,rtBusCommand):
        if tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if tmkCurNumber < tmkCnt:
            return CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtgetcmddata, rtBusCommand)
        return CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtgetcmddata, rtBusCommand)


    def rtenable(self,rtEnable):
        if tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if tmkCurNumber < tmkCnt:
            return CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtenable, rtEnable)
        return CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtenable, rtEnable)


    def TmkOpen(self):
        #int _VTMK4Arg
        #int iTMK
        #String devName

        if _hVTMK4VxD!=0:
            return 0
        tmkCnt = 0
        _hVTMK4VxD = CLibrary.INSTANCE.open("/dev/tmk1553b", 0)
        if _hVTMK4VxD < 0:
            _hVTMK4VxD = 0
        elif ((_VTMK4Arg = CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCGetVersion, 0)) < 0	|| _VTMK4Arg < TMK_VERSION_MIN):
            CLibrary.INSTANCE.close(_hVTMK4VxD)
            _hVTMK4VxD = 0
            return VTMK_BAD_VERSION
        else:
            tmkCnt = CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCtmkgetmaxn) + 1

        tmkUsbCnt = 0
        for iTMK in range(Mil1553LinuxDriver.MAX_TMKUSB_NUMBER):
            _ahVTMK4VxDusb[iTMK] = 0
            tmkUsbNumMap[iTMK] = 0

        for iTMK in range(Mil1553LinuxDriver.MAX_TMKUSB_NUMBER):
            devName = String.format("/dev/tmk1553busb%d", iTMK)
            _ahVTMK4VxDusb[tmkUsbCnt] = CLibrary.INSTANCE.open(devName, 0)
            if (_ahVTMK4VxDusb[tmkUsbCnt] < 0):
                _ahVTMK4VxDusb[tmkUsbCnt] = 0
                continue

            if ((_VTMK4Arg = CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkUsbCnt], TMK_IOCGetVersion, 0)) < 0	|| _VTMK4Arg < TMKUSB_VERSION_MIN):
                CLibrary.INSTANCE.close(_ahVTMK4VxDusb[tmkUsbCnt])
                _ahVTMK4VxDusb[tmkUsbCnt] = 0
                return VTMK_BAD_VERSION
            else:
                CLibrary.INSTANCE.close(_ahVTMK4VxDusb[tmkUsbCnt])
                _ahVTMK4VxDusb[tmkUsbCnt] = 0
            tmkUsbNumMap[tmkUsbCnt] = iTMK
            tmkUsbCnt+=1


        if not(_hVTMK4VxD == 0) and not(tmkUsbCnt == 0):
            return -1
        return 0


    def mtgetsw(self):
        if tmkCurNumber < 0:
            return TMK_BAD_NUMBER
        if tmkCurNumber < tmkCnt:
            return CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCmtgetsw)
        return CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCmtgetsw)


    def tmkconfig(self,tmkNumber):
        if tmkNumber < 0 or tmkNumber >= tmkCnt + tmkUsbCnt:
            return TMK_BAD_NUMBER
        if tmkNumber < tmkCnt:
            if _hVTMK4VxD == 0:
                return TMK_BAD_NUMBER
            tmkCurNumber = tmkNumber
            return CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCtmkconfig, tmkNumber)


        devName = "/dev/tmk1553busb%d"%tmkUsbNumMap[tmkNumber - tmkCnt]
        if (_ahVTMK4VxDusb[tmkNumber - tmkCnt] == 0	or (_ahVTMK4VxDusb[tmkNumber - tmkCnt] = CLibrary.INSTANCE.open(devName, 0)) < 0):
            _ahVTMK4VxDusb[tmkNumber - tmkCnt] = 0
            return TMK_BAD_NUMBER


        Result = CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkNumber - tmkCnt], TMK_IOCtmkconfig, tmkNumber)
        if Result == 0:
            tmkCurNumber = tmkNumber
        return Result


	public int tmkgetmaxn() {
		if (_hVTMK4VxD != 0)
			return (CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCtmkgetmaxn) + tmkUsbCnt)
        else
			return tmkUsbCnt - 1
}

	public int tmkdone(int tmkNumber) {
		int iTMK, bTMK, eTMK
int Result = 0
if (tmkNumber < tmkCnt && tmkNumber != ALL_TMKS) {
			if (_hVTMK4VxD == 0)
				return TMK_BAD_NUMBER
tmkCurNumber = -1
return CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCtmkdone, tmkNumber);
		}
		if (tmkNumber == ALL_TMKS) {
			tmkCurNumber = -1
CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCtmkdone, tmkNumber)
bTMK = 0
eTMK = tmkUsbCnt - 1;
		} else if (tmkNumber < 0 || tmkNumber >= tmkCnt + tmkUsbCnt) {
			return TMK_BAD_NUMBER;
		} else {
			if (tmkNumber == tmkCurNumber)
				tmkCurNumber = -1
bTMK = eTMK = tmkNumber - tmkCnt;
		}
		for (iTMK = bTMK; iTMK <= eTMK; ++iTMK) {
			if (_ahVTMK4VxDusb[iTMK] == 0) {
				Result = CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[iTMK], TMK_IOCtmkdone, iTMK);
				CLibrary.INSTANCE.close(_ahVTMK4VxDusb[iTMK]);
			}
			_ahVTMK4VxDusb[iTMK] = 0
}
		return Result;
	}

	public int tmkselect(int tmkNumber) {
		if (tmkNumber < 0 || tmkNumber >= tmkCnt + tmkUsbCnt)
			return TMK_BAD_NUMBER
if (tmkNumber < tmkCnt) {
			if (_hVTMK4VxD == 0)
				return TMK_BAD_NUMBER
tmkCurNumber = tmkNumber
return (CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCtmkselect, tmkNumber));
		}
		if (_ahVTMK4VxDusb[tmkNumber - tmkCnt] == 1)
			tmkCurNumber = tmkNumber;
		else {
			tmkCurNumber = -1
return TMK_BAD_NUMBER;
		}
		return 0;
	}

	public int tmkselected() {
		if (tmkCurNumber < tmkCnt)
			return CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCtmkselected)
        else
			return tmkCurNumber
}

	public short tmkgetmode() {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return (short) (CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCtmkgetmode))
return (short) CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCtmkgetmode);
	}

	public void tmksetcwbits(short tmkSetControl) {
		if (tmkCurNumber < 0)
			return
if (tmkCurNumber < tmkCnt) {
			CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCtmksetcwbits, tmkSetControl);
			return
}
		CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCtmksetcwbits, tmkSetControl)
}

	public void tmkclrcwbits(short tmkClrControl) {
		if (tmkCurNumber < 0)
			return
if (tmkCurNumber < tmkCnt) {
			CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCtmksetcwbits, tmkClrControl);
			return
}
		CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCtmksetcwbits, tmkClrControl)
}

	public short tmkgetcwbits() {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return (short) (CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCtmkgetcwbits))
return (short) CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCtmkgetcwbits);
	}

	public int tmkwaitevents(int maskEvents, int fWait) {
		int[] _VTMK4Arg = new int[2]
int tmkMask = 0
int DrvMask = 0
int iTMK
int DevMask

if (tmkCnt > 31)
			DevMask = 0xFFFFFFFF
else
			DevMask = (1 << tmkCnt) - 1
if ((maskEvents & DevMask) == 0)// usb only
		{
			_VTMK4Arg[0] = 0
_VTMK4Arg[1] = fWait
for (iTMK = 0; iTMK < tmkUsbCnt; ++iTMK) {
				if ((maskEvents != 0 & (1 << (iTMK + tmkCnt)) != 0) && _ahVTMK4VxDusb[iTMK] != 0)
					_VTMK4Arg[0] |= 1 << tmkUsbNumMap[iTMK]
}
			if (_VTMK4Arg[0] != 0) {
				for (iTMK = 0; iTMK < tmkUsbCnt; ++iTMK) {
					if (_ahVTMK4VxDusb[iTMK] != 0) {
						DrvMask = CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[iTMK], TMK_IOCtmkwaitevents, _VTMK4Arg);
						break
}
				}
				if (DrvMask > 0)
					for (iTMK = 0; iTMK < tmkUsbCnt; ++iTMK) {
						if (DrvMask != 0 & (1 << tmkUsbNumMap[iTMK]) != 0)
							tmkMask |= 1 << (iTMK + tmkCnt);
					}
				else
					return DrvMask;
			}
			return tmkMask
} else if ((maskEvents >> tmkCnt) == 0)// tmk only
		{
			_VTMK4Arg[0] = maskEvents
_VTMK4Arg[1] = fWait
if (_hVTMK4VxD != 0 && _VTMK4Arg[0] != 0)
				tmkMask = CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCtmkwaitevents, _VTMK4Arg)
return tmkMask;
		} else {
			System.out.println("Else");
		}
		return tmkMask;
	}

	public void tmkgetevd(TTmkEventData pEvD) {
		CC cc = new CC()
if (tmkCurNumber < 0) {
			return
} else if (tmkCurNumber < tmkCnt) {
			CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCtmkgetevd, cc.getPointer());
		} else {
			CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCtmkgetevd, cc.getPointer());
		}

		ByteBuffer bb = cc.getPointer().getByteBuffer(0, 6 * 2)
pEvD.nInt = bb.getInt()
pEvD.wMode = bb.getShort()
switch (pEvD.wMode & 0xffff) {
		case BC_MODE:
			switch (pEvD.nInt) {
			case 1:
				pEvD.union.bc.wResult = bb.getShort();
				break
case 2:
				pEvD.union.bc.wResult = bb.getShort()
pEvD.union.bc.wAW1 = bb.getShort()
pEvD.union.bc.wAW2 = bb.getShort()
break;
			case 3:
				pEvD.union.bcx.wResultX = bb.getShort()
pEvD.union.bcx.wBase = bb.getShort()
break;
			case 4:
				pEvD.union.bcx.wBase = bb.getShort()
break;
			}
			break;
		case MT_MODE:
			switch (pEvD.nInt) {
			case 3:
				pEvD.union.mt.wResultX = bb.getShort()
pEvD.union.mt.wBase = bb.getShort();
				break
case 4:
				pEvD.union.mt.wBase = bb.getShort()
break;
			}
			break;
		case RT_MODE:
			switch (pEvD.nInt) {
			case 1:
				pEvD.union.rt.wCmd = bb.getShort();
				break
case 2:
			case 3:
				pEvD.union.rt.wStatus = bb.getShort()
break;
			}
			break;
		case MRT_MODE:
			pEvD.union.mrt.wStatus = bb.getShort()
break;
		case UNDEFINED_MODE:
			pEvD.union.tmk.wRequest = bb.getShort()
break;
		}
	}

	public void tmkgetinfo(TTmkConfigData pConfD) {
		if (tmkCurNumber < 0)
			return
if (tmkCurNumber < tmkCnt) {
			CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCtmkgetinfo, pConfD.getPointer());
			return
}
		CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCtmkgetinfo, pConfD.getPointer())
}

	public int bcreset() {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCbcreset)
return CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCbcreset);
	}

	public int mtreset() {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCmtreset)
return CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCmtreset);
	}

	public int mtdefirqmode(short mtIrqMode) {
		return bcdefirqmode(mtIrqMode);
	}

	public int bcdefirqmode(short bcIrqMode) {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCbcdefirqmode, bcIrqMode)
return CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCbcdefirqmode, bcIrqMode);
	}

	public short bcgetirqmode() {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return (short) CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCbcgetirqmode)
return (short) CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCbcgetirqmode);
	}

	public short mtgetmaxbase() {
		return bcgetmaxbase();
	}

	public short bcgetmaxbase() {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return (short) (CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCbcgetmaxbase))
return (short) (CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCbcgetmaxbase));
	}

	public int mtdefbase(short mtBasePC) {
		return bcdefbase(mtBasePC);
	}

	public int bcdefbase(short bcBasePC) {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCbcdefbase, bcBasePC)
return CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCbcdefbase & 0xffffffff, bcBasePC);
	}

	public short bcgetbase() {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return (short) (CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCbcgetbase))
return (short) (CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCbcgetbase));
	}

	public void bcputw(short bcAddr, short bcData) {
		if (tmkCurNumber < 0)
			return
if (tmkCurNumber < tmkCnt) {
			CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCbcputw, bcAddr | (bcData << 16));
			return
}
		CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCbcputw, bcAddr | (bcData << 16))
}

	public short bcgetw(short bcAddr) {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return (short) CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCbcgetw, bcAddr)
return (short) CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCbcgetw, bcAddr);
	}

	public int bcgetansw(short bcCtrlCode) {
		int _VTMK4Arg
_VTMK4Arg = bcCtrlCode
if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt) {
			CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCbcgetansw, _VTMK4Arg);
			return _VTMK4Arg
}
		CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCbcgetansw, _VTMK4Arg);
		return _VTMK4Arg;
	}

	public void rtgetblk(short rtAddr, Pointer pcBuffer, short cwLength) {
		CLong2 c = new CLong2()
ByteBuffer bb = c.getPointer().getByteBuffer(0, c.size())
bb.putInt((rtAddr | cwLength << 16))
bb.putInt(0)
bb.putLong(Pointer.nativeValue(pcBuffer))
if (tmkCurNumber < 0)
			return
if (tmkCurNumber < tmkCnt) {
			CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtgetblk, c.getPointer());
			return
}
		CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtgetblk, c.getPointer())
}

	public void rtputcmddata(short rtBusCommand, short rtData) {
		if (tmkCurNumber < 0)
			return
if (tmkCurNumber < tmkCnt) {
			CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtputcmddata, rtBusCommand | (rtData << 16));
			return
}
		CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtputcmddata,
				rtBusCommand | (rtData << 16));
	}

	public void rtputblk(short rtAddr, Pointer pcBuffer, short cwLength) {
		CLong2 c = new CLong2()
ByteBuffer bb = c.getPointer().getByteBuffer(0, c.size())
bb.putInt((rtAddr | cwLength << 16))
bb.putInt(0)
bb.putLong(Pointer.nativeValue(pcBuffer))
if (tmkCurNumber < 0)
			return
if (tmkCurNumber < tmkCnt) {
			CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtputblk, c.getPointer());
			return
}
		CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtputblk, c.getPointer())
}

	public void bcputblk(short bcAddr, Pointer pcBuffer, short cwLength) {
		CLong2 c = new CLong2()
ByteBuffer bb = c.getPointer().getByteBuffer(0, c.size())
bb.putInt((bcAddr | cwLength << 16))
bb.putInt(0)
bb.putLong(Pointer.nativeValue(pcBuffer))
if (tmkCurNumber < 0)
			return
if (tmkCurNumber < tmkCnt) {
			CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCbcputblk, c.getPointer());
			return
}
		CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCbcputblk, c.getPointer())
}

	public void mtgetblk(short mtAddr, Pointer pcBuffer, short cwLength) {
		bcgetblk(mtAddr, pcBuffer, cwLength)
}

	public void bcgetblk(short bcAddr, Pointer pcBuffer, short cwLength) {
		CLong2 c = new CLong2()
ByteBuffer bb = c.getPointer().getByteBuffer(0, c.size())
bb.putInt((bcAddr | cwLength << 16))
bb.putInt(0)
bb.putLong(Pointer.nativeValue(pcBuffer))
if (tmkCurNumber < 0)
			return
if (tmkCurNumber < tmkCnt) {
			CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCbcgetblk, c.getPointer());
			return
}
		CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCbcgetblk, c.getPointer())
}

	public int bcdefbus(short bcBus) {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCbcdefbus, bcBus)
return CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCbcdefbus, bcBus);
	}

	public short bcgetbus() {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return (short) CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCbcgetbus)
return (short) CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCbcgetbus);
	}

	public int bcstart(short bcBase, short bcCtrlCode) {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCbcstart, bcBase | (bcCtrlCode << 16))
return CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCbcstart,
				bcBase | (bcCtrlCode << 16));
	}

	public int mtstartx(short mtBase, short mtCtrlCode) {
		return bcstartx(mtBase, mtCtrlCode);
	}

	public int bcstartx(short bcBase, short bcCtrlCode) {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCbcstartx, bcBase | (bcCtrlCode << 16))
return CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCbcstartx,
				bcBase | (bcCtrlCode << 16));
	}

	public int mtdeflink(short mtBase, short mtCtrlCode) {
		return bcdeflink(mtBase, mtCtrlCode);
	}

	public int bcdeflink(short bcBase, short bcCtrlCode) {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCbcdeflink, bcBase | (bcCtrlCode << 16))
return CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCbcdeflink,
				bcBase | (bcCtrlCode << 16));
	}

	public int bcgetlink() {
		class C extends Structure {
			int _VTMK4Arg;
		}
		C c = new C()

if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt) {
			CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCbcgetlink, c.getPointer());
			return c._VTMK4Arg
}
		CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCbcgetlink, c.getPointer());
		return c._VTMK4Arg;
	}

	public int mtstop() {
		return bcstop();
	}

	public short bcstop() {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return (short) (CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCbcstop))
return (short) (CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCbcstop));
	}

	public int bcgetstate() {
		class C extends Structure {
			int _VTMK4Arg;
		}
		C c = new C()
if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt) {
			CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCbcgetstate, c.getPointer());
			return c._VTMK4Arg
}
		CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCbcgetstate, c.getPointer());
		return c._VTMK4Arg;
	}

	public int rtreset() {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtreset)
return CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtreset);
	}

	public int rtdefirqmode(short rtIrqMode) {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return (CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtdefirqmode, rtIrqMode))
return (CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtdefirqmode, rtIrqMode));
	}

	public short rtgetirqmode() {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return (short) (CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtgetirqmode))
return (short) (CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtgetirqmode));
	}

	public int rtdefmode(short rtMode) {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtdefmode, rtMode)
return CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtdefmode, rtMode);
	}

	public short rtgetmode() {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return (short) CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtgetmode)
return (short) CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtgetmode);
	}

	public short rtgetmaxpage() {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return (short) (CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtgetmaxpage))
return (short) (CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtgetmaxpage));
	}

	public int rtdefpage(short rtPage) {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtdefpage, rtPage)
return CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtdefpage, rtPage);
	}

	public short rtgetpage() {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return (short) CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtgetpage)
return (short) CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtgetpage);
	}

	public int rtdefpagepc(short rtPagePC) {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtdefpagepc, rtPagePC)
return CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtdefpagepc, rtPagePC);
	}

	public int rtdefpagebus(short rtPageBus) {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtdefpagebus, rtPageBus)
return CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtdefpagebus, rtPageBus);
	}

	public short rtgetpagepc() {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return (short) CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtgetpagepc)
return (short) CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtgetpagepc);
	}

	public short rtgetpagebus() {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return (short) CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtgetpagebus)
return (short) CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtgetpagebus);
	}

	public int rtdefaddress(short rtAddress) { // TODO: Аномальное включение ОУ (как у rtenable)
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtdefaddress, rtAddress)
return CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtdefaddress, rtAddress);
	}

	public short rtgetaddress() {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return (short) CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtgetaddress)
return (short) CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtgetaddress);
	}

	public void rtdefsubaddr(short rtDir, short rtSubAddr) {
		if (tmkCurNumber < 0)
			return
if (tmkCurNumber < tmkCnt) {
			CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtdefsubaddr, rtDir | (rtSubAddr << 16));
			return
}
		CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtdefsubaddr, rtDir | (rtSubAddr << 16))
}

	public short rtgetsubaddr() {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return (short) (CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtgetsubaddr))
return (short) (CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtgetsubaddr));
	}

	public void rtputw(short rtAddr, short rtData) {
		if (tmkCurNumber < 0)
			return
if (tmkCurNumber < tmkCnt) {
			CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtputw, rtAddr | (rtData << 16));
			return
}
		CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtputw, rtAddr | (rtData << 16))
}

	public short rtgetw(short rtAddr) {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return (short) CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtgetw, rtAddr)
return (short) CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtgetw, rtAddr);
	}

	public void rtsetanswbits(short rtSetControl) {
		if (tmkCurNumber < 0)
			return
if (tmkCurNumber < tmkCnt) {
			CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtsetanswbits, rtSetControl);
			return
}
		CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtsetanswbits, rtSetControl)
}

	public void rtclranswbits(short rtClrControl) {
		if (tmkCurNumber < 0)
			return
if (tmkCurNumber < tmkCnt) {
			CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtclranswbits, rtClrControl);
			return
}
		CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtclranswbits, rtClrControl)
}

	public short rtgetanswbits() {
		if (tmkCurNumber < 0)
			return TMK_BAD_NUMBER
if (tmkCurNumber < tmkCnt)
			return (short) CLibrary.INSTANCE.ioctl(_hVTMK4VxD, TMK_IOCrtgetanswbits)
return (short) CLibrary.INSTANCE.ioctl(_ahVTMK4VxDusb[tmkCurNumber - tmkCnt], TMK_IOCrtgetanswbits);
	}

	@Override
	public void TmkClose() {
		// TODO Auto-generated method stub
	}

	@Override
	public void tmkdefevent(HANDLE hEvent, boolean fEventSet) {
		// TODO Auto-generated method stub
	}

	@Override
	public void bc_def_tldw(short wTLDW) {
		// TODO Auto-generated method stub

	}

	@Override
	public void bc_enable_di() {
		// TODO Auto-generated method stub

	}

	@Override
	public void bc_disable_di() {
		// TODO Auto-generated method stub
	}

	@Override
	public void rtgetflags(Pointer pcBuffer, short rtDir, short rtFlagMin, short rtFlagMax) {
		// TODO Auto-generated method stub

	}

	@Override
	public void rtputflags(Pointer pcBuffer, short rtDir, short rtFlagMin, short rtFlagMax) {
		// TODO Auto-generated method stub

	}

	@Override
	public void rtsetflag() {
		// TODO Auto-generated method stub

	}

	@Override
	public void rtclrflag() {
		// TODO Auto-generated method stub

	}

	@Override
	public short rtgetflag(short rtDir, short rtSubAddr) {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public short rtgetstate() {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public void rtlock(short rtDir, short rtSubAddr) {
		// TODO Auto-generated method stub

	}

	@Override
	public void rtunlock() {
		// TODO Auto-generated method stub

	}
}
