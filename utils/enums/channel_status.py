from enum import Enum


class ChannelType(str, Enum):
    TELEGRAM = "telegram"


class ChannelStatus(str, Enum):
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"
    ERROR = "error"
