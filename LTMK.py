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
    def _IOC(dir, type, nr, size):
        return (dir << _IOC_DIRSHIFT) | (type << _IOC_TYPESHIFT) | (nr << _IOC_NRSHIFT) | (size << _IOC_SIZESHIFT)

    @staticmethod
    def _IOC_TYPECHECK(size):
        return size

    @staticmethod
    def _IO(type, nr):
        return _IOC(_IOC_NONE, type, nr, 0)

    @staticmethod
    def _IOR(type, nr, size):
        return _IOC(_IOC_READ, type, nr, (_IOC_TYPECHECK(size)))

    @staticmethod
    def _IOW(type, nr, size):
        return _IOC(_IOC_WRITE, type, nr, (_IOC_TYPECHECK(size)))

    @staticmethod
    def _IOWR(type, nr, size):
        return _IOC(_IOC_READ | _IOC_WRITE, type, nr, (_IOC_TYPECHECK(size)))

    @staticmethod
    def _IOR_BAD(type, nr, size):
        return _IOC(_IOC_READ, type, nr, size)

    @staticmethod
    def _IOW_BAD(type, nr, size):
        return _IOC(_IOC_WRITE, type, nr, size)

    @staticmethod
    def _IOWR_BAD(type, nr, size):
        return _IOC(_IOC_READ | _IOC_WRITE, type, nr, size)

    '''/* used to decode ioctl numbers.. */'''

    @staticmethod
    def _IOC_DIR(nr):
        return (nr >> _IOC_DIRSHIFT) & _IOC_DIRMASK

    @staticmethod
    def _IOC_TYPE(nr):
        return (nr >> _IOC_TYPESHIFT) & _IOC_TYPEMASK

    @staticmethod
    def _IOC_NR(nr):
        return (nr >> _IOC_NRSHIFT) & _IOC_NRMASK

    @staticmethod
    def _IOC_SIZE(nr):
        return (nr >> _IOC_SIZESHIFT) & _IOC_SIZEMASK

    '''/* ...and for the drivers/sound files... */'''

    @staticmethod
    def IOC_IN():
        return _IOC_WRITE << _IOC_DIRSHIFT

    @staticmethod
    def IOC_OUT():
        return _IOC_READ << _IOC_DIRSHIFT

    @staticmethod
    def IOC_INOUT():
        return (_IOC_WRITE | _IOC_READ) << _IOC_DIRSHIFT

    @staticmethod
    def IOCSIZE_MASK():
        return _IOC_SIZEMASK << _IOC_SIZESHIFT

    @staticmethod
    def IOCSIZE_SHIFT():
        return _IOC_SIZESHIFT
