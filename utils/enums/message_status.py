from enum import Enum


class SenderType(str, Enum):
    CLIENT = "client"
    EMPLOYEE = "employee"
    HUMAN = "human"
