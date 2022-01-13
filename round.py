import random

class Round:
    exit_option = 'Leave game'
    times_up_message = "Time's up! Try to be quicker next time"
    round_options = [exit_option]

    messages = {'correct' : "Correct answer!",
    'wrong' : "Wrong answer",
    'leave' : "Leaving game...",
    'reward': "Congratulations! You have earned: ",
    'points': " points"}

    def __init__(self, view, input_getter, player, question, reward):
        self.view = view
        self.input_getter = input_getter
        #self.answer_processor = answer_processor
        self.player = player
        self.question = question
        self.reward = reward
        self.sentence = self.question.get_sentence()
        self.options = self.options_list()

    def exit(self):
        self.view.clean()
        return False

    def times_up(self):
        self.view()
        return False

    def give_reward(self):
        self.player.add_reward(self.reward)
        #message = "a"
        print(Round.messages['reward'] + str(self.reward.get_points()) + Round.messages['points'])

    def check_answer(self, input):
        index = int(input) - 1
        if self.options[index] == self.question.get_answer():
            print(Round.messages['correct'])
            self.give_reward()
            return True
        elif self.options[index] == Round.exit_option:
            print(Round.messages['leave'])
            return False
        else:
            print(Round.messages['wrong'])
            return False

    def options_list(self):
        options = self.question.get_options()
        random.shuffle(options)
        options.extend(Round.round_options)
        return options

    def run(self):

        self.view.show(self.sentence, "sentence")
        self.view.show(self.options, "options")
        user_input = self.input_getter.get_input(9)
        result = self.check_answer(user_input)
        return result


