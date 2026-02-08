from enum import Enum

class Pins(Enum):
    SPAIR = "/"
    STRIKE = "X"
    FOUL = "0"
    TOTAL_PINS = 10
    ZERO = 0
    ONE = 1
    LAST_FRAME_ROLLS = 3
    ROLLS_STRIKE = 1
    NORMAL_FRAMES_ROLLS = 2
