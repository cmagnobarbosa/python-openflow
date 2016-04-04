from struct import pack
from struct import unpack
from struct import unpack_from
from common import base
from common import exceptions


# TODO: Refactor unpack methods to return the unpacked object
#       instead of being an inplace method.


class UBInt8(base.GenericType):
    """
    Format character for an Unsigned Char. Class for an 8 bytes
    Unsigned Integer.
    """
    fmt = "!B"


class UBInt8Array(base.GenericType):
    """
    Creates an Array of Unsigned Integer of 8 bytes.
    """
    def __init__(self, value=None, length=0):
        if value:
            self.value = value
        self.length = length
        self.fmt = "!%d%c" % (self.length, 'B')

    def unpack(self, buff, offset=0):
        """
        Unpack a buff and stores at value property.
        Keyword arguments:
            buff -- Buffer where data is located.
            offset -- Where data stream begins.
        """
        self.value = unpack_from(self.fmt, buff, offset)

    def pack(self):
        """
        Here we need a pointer, self.value is a tuple and is expanded to
        args.
        """
        return pack(self.fmt, *self.value)


class UBInt16(base.GenericType):
    """
    Format character for an Unsigned Short. Class for an 16 bytes
    Unsigned Integer.
    """
    fmt = "!H"


class UBInt32(base.GenericType):
    """
    Format character for an Unsigned Int. Class for an 32 bytes
    Unsigned Integer.
    """
    fmt = "!I"


class UBInt64(base.GenericType):
    """
    Format character for an Unsigned Long Long. Class for an 64 bytes
    Unsigned Integer.
    """
    fmt = "!Q"


class Char(base.GenericType):
    """

    """
    def __init__(self, value=None, length=0):
        if value:
            self.value = value
        self.length = length
        self.fmt = '!%d%c' % (self.length, 's')
