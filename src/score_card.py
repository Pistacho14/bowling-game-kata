from functools import reduce
from .pins import Pins


class Score_card:
    def __init__(self, pins):
        self.pins = pins.replace("-", "0")  # Reemplazar los fouls por 0
        self.frames = []
        self.numerical_frames = []

#-------------------------------------------------------------------------------------------------
    def get_pins(self):
        return self.pins

    def get_frames(self):
        return self.frames

    def get_numerical_frames(self):
        return self.numerical_frames

    def set_pins(self, pins):
        self.pins = pins

    def set_frames(self, frames):
        self.frames = frames
# ------------------------------------------------------------------------------------------------

    def _split_frames(self):
        index = 0

        for _ in range(9):
            roll = self.pins[index]

            if roll == Pins.STRIKE.value[0]:
                frame = [Pins.STRIKE.value[0]]
                numerical_frame = [Pins.TEN.value]
                index += Pins.ROLLS_STRIKE.value

            elif self.pins[index + 1] == Pins.SPAIR.value[0]:
                frame = [roll, Pins.SPAIR.value[0]]
                numerical_frame = [int(roll), Pins.TEN.value - int(roll)]
                index += Pins.NORMAL_FRAMES_ROLLS.value
                
            else:
                frame = [roll, self.pins[index + 1]]
                numerical_frame = [int(roll), int(self.pins[index + 1])]
                index += Pins.NORMAL_FRAMES_ROLLS.value

            self.frames.append(frame)
            self.numerical_frames.append(numerical_frame)

        last_frame = list(self.pins[index : index + Pins.ROLLS_LAST_FRAME.value])

        last_numerical_frame = []

        for roll in self.pins[index : index + Pins.ROLLS_LAST_FRAME.value]:
            if roll == Pins.STRIKE.value[0]:
                last_numerical_frame.append(Pins.TEN.value)
            elif roll == Pins.SPAIR.value[0]:
                last_numerical_frame.append(Pins.TEN.value - last_numerical_frame[-1])
            else:
                last_numerical_frame.append(int(roll))

        self.frames.append(last_frame)
        self.numerical_frames.append(last_numerical_frame)

        return self.frames, self.numerical_frames
#-------------------------------------------------------------------------------------------------


    def score_calculator(self):
        score = 0
        score_card_index = 0
        for frame in self.frames:
            if Score_card._common_roll(frame):
                score += reduce(lambda x, y: int(x) + int(y), frame)
                score_card_index += 1
            elif frame[-1] == Pins.SPAIR.value[0]:
                score += 10 + int(self.get_frames()[score_card_index + 1][0])
                score_card_index += 1
            else:
                continue

        return score

    @staticmethod
    def _common_roll(frame):
        return frame[0].isnumeric() and frame[1].isnumeric()

    def __repr__(self):
        return Score_card.get_frames()
