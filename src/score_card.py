from functools import reduce
from .pins import Pins


class Score_card:
    def __init__(self, pins):
        self.pins = pins.replace("-", "0")  # Reemplazar los fouls por 0
        self.frames = []
        self.numerical_frames = []

    # -------------------------------------------------------------------------------------------------
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

    # -------------------------------------------------------------------------------------------------

    def score_calculator(self):
        score = 0
        score_card_index = 0
        for frame in self.frames[:-1]:
            if Score_card._common_roll(frame):
                score += reduce(
                    lambda x, y: x + y,
                    Score_card.get_numerical_frames(self)[score_card_index],
                )
                score_card_index += 1
            elif Score_card._spair_roll(frame):
                score += (
                    10 + Score_card.get_numerical_frames(self)[score_card_index + 1][0]
                )
                score_card_index += 1
            else:
                if Score_card._check_next_frame(self, score_card_index):
                    score += 10 + sum(
                        Score_card.get_numerical_frames(self)[score_card_index + 1][0:2]
                    )
                    score_card_index += 1
                else:
                    score += (
                        10
                        + Score_card.get_numerical_frames(self)[score_card_index + 1][0]
                        + Score_card.get_numerical_frames(self)[score_card_index + 2][0]
                    )
                    score_card_index += 1

        score += sum(Score_card.get_numerical_frames(self)[-1])

        return score

    def _check_next_frame(self, score_card_index):
        return (
            True
            if len(Score_card.get_numerical_frames(self)[score_card_index + 1]) >= 2
            else False
        )

    @staticmethod
    def _common_roll(frame):
        return frame[0].isnumeric() and frame[1].isnumeric()

    @staticmethod
    def _spair_roll(frame):
        return frame[-1] == Pins.SPAIR.value[0]

    def __repr__(self):
        return Score_card.get_frames()
