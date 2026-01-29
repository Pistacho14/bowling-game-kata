class Score_card:

    def __init__(self, score_card):
        self.pins = score_card
        self.pins_list = []

    def __score_card_cleaner(self):
        counter = 0
        index = 0
        MAX_ROUNDS = 10
        while counter < MAX_ROUNDS:
            self.pins_list.append(list(self.pins[index:index+1]))
            counter += 1
        self.pins_list.append(list(self.pins[17::]))
        
        return self.pins_list
