class Score_card:

    SPAIR = "/"
    STRIKE = "X"
    FOUL = "-"
    ROLLS_LAST_FRAME = 3
    ROLLS_STRIKE = 1
    NORMAL_FRAMES_ROLLS = 2

    def __init__(self, pins):
        self.pins = pins
        self.frames = []

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

        last_frame = list(self.pins[index:index + Score_card.ROLLS_LAST_FRAME])
        self.frames.append(last_frame)

        return self.frames