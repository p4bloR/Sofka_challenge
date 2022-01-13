from os import system, name


class View:

    def __init__(self):
        self.input_getter = None

    def clear(self):

        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux
        else:
            _ = system('clear')

    def show(self, content, type = "sentence"):
        #self.clear()
        if type == "options":
            i = 1
            for item in content:
                print(str(i) + " " + item)
                i += 1
        elif type == "list":
            for item in content:
                print(item)

        elif type == "sentence":
            print(content)