from driverLinux import Mil1553LinuxDriver


class Mil1553Device:
    def __init__(self, cardnumber=0):
        self.cardnumber = cardnumber
        self.driver = Mil1553LinuxDriver()

    def init_as(self, mode="BC"):
        result = self.driver.tmk_open()
        if result != 0:
            raise ("Ошибка TmkOpen ", result)
        result = self.driver.tmkconfig(self.cardNumber)
        if result != 0:
            raise ("Ошибка tmkconfig ", result)
