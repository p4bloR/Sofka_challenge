from inputimeout import inputimeout, TimeoutOccurred

class Controller:
    #def __init__(self, model, view):
    #    self.model = model
    #    self.view = view
    def __init__(self):
        self.name = 'lala'

    def alive(self):
        return 'i am alive'

    def get_user_input(self):
        print("getting user input")
        try:
          something = inputimeout(prompt='>>', timeout=5)
          print(something)
          print("Time's out")
        except TimeoutOccurred:
            something = 'something'
            print(something)
