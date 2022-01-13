from menu import Menu

class ScoreboardMenu(Menu):
    def __init__(self):
        self.sentences = None
        self.options = None
        self.view = None
        self.input_getter = None
        self.model = None

    def set_variables(self, sentences, options: dict, view, input_getter, model):
        self.sentences = sentences
        self.options = options
        self.view = view
        self.input_getter = input_getter
        self.model = model

    def get_scores(self):
        scores = self.model.get_scoreboard()
        return scores

    def show(self):
        scores = self.get_scores()
        self.view.show(self.sentences, "sentence")
        self.view.show(scores, "list")
        self.view.show(self.options.keys(), "options")
        self.process_input()

    def run(self):
        self.show()