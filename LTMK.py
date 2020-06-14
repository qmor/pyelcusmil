'''**
 * Порт набора функций из файлов ltmk.c, ltmk.h
 * @author qmor
 *
 *'''




class ioctl(object):
    _IOC_NRBITS = 8
    _IOC_TYPEBITS = 8
    _IOC_SIZEBITS = 14
    _IOC_DIRBITS = 2
    _IOC_NRMASK = ((1 << _IOC_NRBITS) - 1)
    _IOC_TYPEMASK = ((1 << _IOC_TYPEBITS) - 1)
    _IOC_SIZEMASK = ((1 << _IOC_SIZEBITS) - 1)
    _IOC_DIRMASK = ((1 << _IOC_DIRBITS) - 1)
    _IOC_NRSHIFT = 0
    _IOC_TYPESHIFT = (_IOC_NRSHIFT + _IOC_NRBITS)
    _IOC_SIZESHIFT = (_IOC_TYPESHIFT + _IOC_TYPEBITS)
    _IOC_DIRSHIFT = (_IOC_SIZESHIFT + _IOC_SIZEBITS)

    _IOC_NONE = 0
    _IOC_WRITE = 1
    _IOC_READ = 2

    @staticmethod
    def _IOC(direction, _type, nr, size):
        return (direction << ioctl._IOC_DIRSHIFT) | (_type << ioctl._IOC_TYPESHIFT) | (nr << ioctl._IOC_NRSHIFT) | (
                    size << ioctl._IOC_SIZESHIFT)

    @staticmethod
    def _IOC_TYPECHECK(size):
        return size

    @staticmethod
    def _IO(type_, nr):
        return ioctl._IOC(ioctl._IOC_NONE, type_, nr, 0)

    @staticmethod
    def _IOR(type_, nr, size):
        return ioctl._IOC(ioctl._IOC_READ, type_, nr, (ioctl._IOC_TYPECHECK(size)))

    @staticmethod
    def _IOW(type_, nr, size):
        return ioctl._IOC(ioctl._IOC_WRITE, type_, nr, (ioctl._IOC_TYPECHECK(size)))

    @staticmethod
    def _IOWR(type_, nr, size):
        return ioctl._IOC(ioctl._IOC_READ | ioctl._IOC_WRITE, type_, nr, (ioctl._IOC_TYPECHECK(size)))

    @staticmethod
    def _IOR_BAD(type_, nr, size):
        return ioctl._IOC(ioctl._IOC_READ, type_, nr, size)

    @staticmethod
    def _IOW_BAD(type_, nr, size):
        return ioctl._IOC(ioctl._IOC_WRITE, type_, nr, size)

    @staticmethod
    def _IOWR_BAD(type_, nr, size):
        return ioctl._IOC(ioctl._IOC_READ | ioctl._IOC_WRITE, type_, nr, size)

    '''/* used to decode ioctl numbers.. */'''

    @staticmethod
    def _IOC_DIR(nr):
        return (nr >> ioctl._IOC_DIRSHIFT) & ioctl._IOC_DIRMASK

    @staticmethod
    def _IOC_TYPE(nr):
        return (nr >> ioctl._IOC_TYPESHIFT) & ioctl._IOC_TYPEMASK

    @staticmethod
    def _IOC_NR(nr):
        return (nr >> ioctl._IOC_NRSHIFT) & ioctl._IOC_NRMASK

    @staticmethod
    def _IOC_SIZE(nr):
        return (nr >> ioctl._IOC_SIZESHIFT) & ioctl._IOC_SIZEMASK

    '''/* ...and for the drivers/sound files... */'''

    @staticmethod
    def IOC_IN():
        return ioctl._IOC_WRITE << ioctl._IOC_DIRSHIFT

    @staticmethod
    def IOC_OUT():
        return ioctl._IOC_READ << ioctl._IOC_DIRSHIFT

    @staticmethod
    def IOC_INOUT():
        return (ioctl._IOC_WRITE | ioctl._IOC_READ) << ioctl._IOC_DIRSHIFT

    @staticmethod
    def IOCSIZE_MASK():
        return ioctl._IOC_SIZEMASK << ioctl._IOC_SIZESHIFT

    @staticmethod
    def IOCSIZE_SHIFT():
        return ioctl._IOC_SIZESHIFT
