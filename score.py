from reward import Reward

class Score(Reward):
    def __init__(self, points, decrement):
        super().__init__(points)
        self.decrement = self.points * (1 / decrement)

    def decrease(self):
        self.points -= int(self.decrement)
