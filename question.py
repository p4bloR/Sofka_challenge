class Question:
    def __init__(self, categories, sentence, answer: str, alternatives, difficulty):
        self.categories = categories
        self.sentence = sentence
        self.answer = answer
        self.alternatives = alternatives
        self.difficulty = difficulty
        self.alternatives.append(self.answer)
        self.options = self.alternatives


    def get_sentence(self):
        return self.sentence

    def get_answer(self):
        return self.answer

    def get_difficulty(self):
        return self.difficulty

    """ def fill_options(self):

    return options_list
    dict = {0: self.answer}
    i = 1
    for alternative in self.alternatives:
    dict[str(i)] = alternative
    i += 1
    return dict
    """
    def get_options(self):
        return self.options
