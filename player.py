import datetime

class Player:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.rewards = []
        self.score = 0


    def get_score(self):
        return self.score

    def add_reward(self, reward):
        self.score += reward.get_points()
        print("score", self.score)
        self.rewards.append(reward)
        self.model.save_player_data(self.get_data())

    def get_name(self):
        return self.name

    def get_reward(self):
        return self.rewards

    def get_data(self):
        #ts = str(datetime.datetime.now().timestamp())
        ts = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        return [ts, str(self.score), self.name]


