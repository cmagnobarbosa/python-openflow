"""Defines Header classes and related items."""

# System imports
import enum
from random import randint

# Third-party imports

# Local source tree imports
from pyof.v0x01.foundation import base
from pyof.v0x01.foundation import basic_types

__all__ = ('Header', 'Type')

# Max xid of a message considering it's size (UBInt32 on v0x01)
MAXID = 2147483647

# Enums


class Type(enum.Enum):
    """Enumeration of Message Types."""

    # Symetric/Immutable messages
    OFPT_HELLO = 0
    OFPT_ERROR = 1
    OFPT_ECHO_REQUEST = 2
    OFPT_ECHO_REPLY = 3
    OFPT_VENDOR = 4

    # Switch configuration messages
    # Controller/Switch messages
    OFPT_FEATURES_REQUEST = 5
    OFPT_FEATURES_REPLY = 6
    OFPT_GET_CONFIG_REQUEST = 7
    OFPT_GET_CONFIG_REPLY = 8
    OFPT_SET_CONFIG = 9

    # Async messages
    OFPT_PACKET_IN = 10
    OFPT_FLOW_REMOVED = 11
    OFPT_PORT_STATUS = 12

    # Controller command messages
    # Controller/switch message
    OFPT_PACKET_OUT = 13
    OFPT_FLOW_MOD = 14
    OFPT_PORT_MOD = 15

    # Statistics messages
    # Controller/Switch message
    OFPT_STATS_REQUEST = 16
    OFPT_STATS_REPLY = 17

    # Barrier messages
    # Controller/Switch message
    OFPT_BARRIER_REQUEST = 18
    OFPT_BARRIER_REPLY = 19

    # Queue Configuration messages
    # Controller/Switch message
    OFPT_QUEUE_GET_CONFIG_REQUEST = 20
    OFPT_QUEUE_GET_CONFIG_REPLY = 21


# Classes


class Header(base.GenericStruct):
    """Representation of an OpenFlow message Header.

    Args:
        message_type (Type): Type of the message.
        xid (int): ID of the message.
        length (int): Length of the message, including the header itself.
    """

    version = basic_types.UBInt8(base.OFP_VERSION)
    message_type = basic_types.UBInt8(enum_ref=Type)
    length = basic_types.UBInt16()
    xid = basic_types.UBInt32()

    def __init__(self, message_type=None, length=None, xid=randint(0, MAXID)):
        super().__init__()
        self.message_type = message_type
        self.length = length
        self.xid = xid
