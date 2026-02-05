from functools import reduce

class Score_card:
    SPAIR = "/"
    STRIKE = "X"
    FOUL = "-"
    ROLLS_LAST_FRAME = 3
    ROLLS_STRIKE = 1
    NORMAL_FRAMES_ROLLS = 2

    def __init__(self, pins):
        self.pins = pins.replace("-", "0") #Reemplazar los fouls por 0
        self.frames = []

    def get_pins(self):
        return self.pins

    def get_frames(self):
        return self.frames

    def set_pins(self, pins):
        self.pins = pins

    def set_frames(self, frames):
        self.frames = frames

    def _split_frames(self):
        index = 0

        for _ in range(9):
            roll = self.pins[index]

            if roll == "X":
                frame = ["X"]
                index += Score_card.ROLLS_STRIKE
            else:
                frame = [roll, self.pins[index + 1]]
                index += Score_card.NORMAL_FRAMES_ROLLS

            self.frames.append(frame)

        last_frame = list(self.pins[index : index + Score_card.ROLLS_LAST_FRAME])
        self.frames.append(last_frame)

        return self.frames

    def score_calculator(self):
        score = 0
        score_card_index = 0
        for frame in self.frames:
            if frame[0].isnumeric() and frame[1].isnumeric():
                score += reduce(lambda x, y: int(x) + int(y), frame)
                score_card_index += 1
            elif frame[-1] == Score_card.SPAIR:
                score += 10 + int(self.get_frames()[score_card_index + 1][0])
                score_card_index += 1
            else:
                continue

        return score
