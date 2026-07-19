from enum import Enum


class DialogStatus(str, Enum):
    ACTIVE = "active"
    RESOLVED = "resolved"
    NEEDS_HUMAN = "needs_human"
