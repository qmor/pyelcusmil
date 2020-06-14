class Mil1553WindowsDriver:
    MAX_TMKUSB_NUMBER = 8 - 1
    def __init__(self):
        self.tmkUsbCnt = 0
        self.tmkCnt = 0
        self.tmkCurNumber = -1
        self.tmkUsbNumMap = [0 for _ in range(Mil1553WindowsDriver.MAX_TMKUSB_NUMBER + 1)]
        self._ahVTMK4VxDusb = [0 for _ in range(Mil1553WindowsDriver.MAX_TMKUSB_NUMBER + 1)]

    def rtbusy(self):
        return 0

    def rtgetcmddata(self, rtBusCommand):
        return 0

    def rtenable(self, rtEnable):
        return 0

    def tmk_open(self):
        return 0

    def mtgetsw(self):
        return 0

    def tmkconfig(self, tmkNumber):
        return 0

    def tmkgetmaxn(self):
        return 0

    def tmkdone(self, tmkNumber):
        return 0

    def tmkselect(self, tmkNumber):
        return 0

    def tmkselected(self):
        return self.tmkCurNumber

    def tmkgetmode(self):
        return 0

    def tmksetcwbits(self, tmkSetControl):
        return

    def tmkclrcwbits(self, tmkClrControl):
        return

    def tmkgetcwbits(self):
        return 0

    def tmkwaitevents(self, maskEvents, fWait):
        return 0

    def tmkgetevd(self, pEvD):
        return

    def tmkgetinfo(self, pConfD):
        return

    def bcreset(self):
        return 0

    def mtreset(self):
        return 0

    def mtdefirqmode(self, mtIrqMode):
        return self.bcdefirqmode(mtIrqMode)

    def bcdefirqmode(self, bcIrqMode):
        return 0

    def bcgetirqmode(self):
        return 0

    def mtgetmaxbase(self):
        return self.bcgetmaxbase()

    def bcgetmaxbase(self):
        return 0

    def mtdefbase(self, mtBasePC):
        return self.bcdefbase(mtBasePC)

    def bcdefbase(self, bcBasePC):
        return 0

    def bcgetbase(self):
        return 0

    def bcputw(self, bcAddr, bcData):
        return

    def bcgetw(self, bcAddr):
        return 0

    def bcgetansw(self, bcCtrlCode):
        return 0

    def rtgetblk(self, rtAddr, pcBuffer, cwLength):
        return

    def rtputcmddata(self, rtBusCommand, rtData):
        return

    def rtputblk(self, rtAddr, pcBuffer, cwLength):
        return

    def bcputblk(self, bcAddr, pcBuffer, cwLength):
        return

    def mtgetblk(self, mtAddr, pcBuffer, cwLength):
        self.bcgetblk(mtAddr, pcBuffer, cwLength)

    def bcgetblk(self, bcAddr, pcBuffer, cwLength):
        return

    def bcdefbus(self, bcBus):
        return 0

    def bcgetbus(self):
        return 0

    def bcstart(self, bcBase, bcCtrlCode):
        return 0

    def mtstartx(self, mtBase, mtCtrlCode):
        return self.bcstartx(mtBase, mtCtrlCode)

    def bcstartx(self, bcBase, bcCtrlCode):
        return 0

    def mtdeflink(self, mtBase, mtCtrlCode):
        return self.bcdeflink(mtBase, mtCtrlCode)

    def bcdeflink(self, bcBase, bcCtrlCode):
        return 0

    def bcgetlink(self):
        return 0

    def mtstop(self):
        return self.bcstop()

    def bcstop(self):
        return 0

    def bcgetstate(self):
        return 0

    def rtreset(self):
        return 0

    def rtdefirqmode(self, rtIrqMode):
        return 0

    def rtgetirqmode(self):
        return 0

    def rtdefmode(self, rtMode):
        return 0

    def rtgetmode(self):
        return 0

    def rtgetmaxpage(self):
        return 0

    def rtdefpage(self, rtPage):
        return 0

    def rtgetpage(self):
        return 0

    def rtdefpagepc(self, rtPagePC):
        return 0

    def rtdefpagebus(self, rtPageBus):
        return 0

    def rtgetpagepc(self):
        return 0

    def rtgetpagebus(self):
        return 0

    def rtdefaddress(self, rtAddress):
        return 0

    def rtgetaddress(self):
        return 0

    def rtdefsubaddr(self, rtDir, rtSubAddr):
        return

    def rtgetsubaddr(self):
        return 0

    def rtputw(self, rtAddr, rtData):
        return

    def rtgetw(self, rtAddr):
        return 0

    def rtsetanswbits(self, rtSetControl):
        return

    def rtclranswbits(self, rtClrControl):
        return

    def rtgetanswbits(self):
        return 0