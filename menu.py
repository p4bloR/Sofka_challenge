class Menu:

    messages = {"invalid": "Invalid input, try again."}

    def __init__(self):
        self.sentences = None
        self.options = None
        self.view = None
        self.input_getter = None

#    def __init__(self, sentences = None, options = None, view = None, input_getter= None):
#        self.sentences = sentences
#        self.options = options
#        self.view = view
#        self.input_getter = input_getter

    def set_variables(self, sentences , options , view , input_getter):
        self.sentences = sentences
        self.options = options
        self.view = view
        self.input_getter = input_getter


    def show(self):
        self.view.show(self.sentences, "sentence")
        self.view.show(self.options.keys(), "options")

    def process_input(self):
        user_input = self.input_getter.get_user_input()
        if user_input.isnumeric() and int(user_input) <= len(self.options):
            keys = list(self.options.keys())
            selected_key = keys[int(user_input) - 1]
            self.options[selected_key].run()
        else:
            self.view.show(Menu.messages["invalid"])

    def run(self):
        self.show()
        self.process_input()