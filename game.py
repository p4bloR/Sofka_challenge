import random
from round import Round
from reward import Reward
from question import Question
import time

class Game:
    def __init__(self, player, model, view, input_getter, categories):
        self.player = player
        self.model = model
        self.view = view
        self.categories = None
        self.rounds = 5 #giving some default values to avoid errors
        self.diff_base = 1
        self.diff_max = 5
        self.diff_step = None
        self.reward_base = None
        self.reward_multiplier = None
        self.input_getter = input_getter
        self.categories = categories
        self.back_to_menu = None



#    def set_variables(self, view, player, input_getter, model, categories):
#        self.player = player
#        self.model = model
#        self.categories = categories

    def get_random_category(self):
        return random.choice(self.categories)

    def get_questions_data(self, categories, rounds = 5, diff_base = 1, diff_max = 5):
        #after how many rounds should the difficulty go up
        diff_step = diff_max / rounds
        quantity = diff_step
        difficulty = diff_base
        question_list = []

        for i in range(1, rounds + 1):
            #get all the questions with certain difficulty
            questions = self.model.get_random_question(categories, difficulty, quantity)
            question_list.append(questions)
            #once diff_max is reached get the remaining questions
            if difficulty == diff_max:
                quantity = rounds - diff_step * diff_max
                question_list.append(self.model.get_random_question(categories, difficulty, quantity))
            difficulty += 1

        return question_list

    def process_question_data(self, question_data):
        questions_list = []
        for i in range(len(question_data) - 1):
            questions_list.append(question_data[i][0])

        for q in questions_list:
            q = list(q)
        return questions_list


    def generate_rounds(self, question_data):
        win = True
        question_list = self.process_question_data(question_data)
        points = self.reward_base
        for q in question_list:
            points *= self.reward_multiplier
            reward = Reward(points)
            #categories, sentence, answer: str, alternatives, difficulty
            question = Question(q[1], q[0], q[3], list(q[4:6]), q[2])
            round =  Round(self.view, self.input_getter, self.player, question, reward)
            if not round.run():
                win = False
                break
            time.sleep(3)
        if win:
            self.view.show("Congratulations, you won this game!", "sentence")
            time.sleep(3)


    def settings(self, rounds, diff_base, diff_max, reward_base, reward_multiplier, back_to_menu):
        self.rounds = rounds
        self.diff_base = diff_base
        self.diff_max = diff_max
        self.reward_base = reward_base
        self.reward_multiplier = reward_multiplier
        self.back_to_menu = back_to_menu

    def run(self):
        category = self.get_random_category()

        self.view.show("Your category is: " + category +"!", "sentence")
        time.sleep(3)
        question_data = self.get_questions_data(category, self.rounds, self.diff_base, self.diff_max)
        self.generate_rounds(question_data)
        self.back_to_menu.run()
        #self.get_questions_data(self.categories, self.rounds, self.diff_base, self.diff_max)
        #

    def save_player_data(self):
        data = self.player.get_data()
        self.model.save_score(data)
