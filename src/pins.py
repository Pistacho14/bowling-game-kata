from enum import Enum

class Pins(Enum):
    SPAIR = ["/", lambda x, y: x - y]
    STRIKE = ["X", 10]
    FOUL = "0"
    TEN = 10
    ZERO = 0
    ONE = 1
    ROLLS_LAST_FRAME = 3
    ROLLS_STRIKE = 1
    NORMAL_FRAMES_ROLLS = 2
