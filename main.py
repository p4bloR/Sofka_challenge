from player import Player
from score import Score
from controller import Controller
from model import Model
from round import Round
from view import View
from inputgetter import InputGetter
from question import Question
from timeoutgetter import TimeOutGetter
from menu import Menu
from game import Game
from scoreboardmenu import ScoreboardMenu
from exit import Exit

view = View()
timeoutgetter = TimeOutGetter()

categories = ["History", "Sports", "Videogames", "Science", "Cinema"]

exit = Exit()
model = Model()
input_getter = InputGetter()
player = Player(input_getter.get_user_input("Enter your name: "), model)
main_menu = Menu()
scoreboard_menu = ScoreboardMenu()
game = Game(player, model, view, timeoutgetter, categories)
game.settings(5, 1, 5, 100, 1.5, main_menu)

scoreboard_sentence = "Scoreboard\r\n   Name     Score       Date"
scoreboard_options = {"Return to main menu": main_menu}

main_sentence = "Welcome to the Trivia Game"
main_options = {"Play": game, "See scoreboard": scoreboard_menu, "Exit": exit}

scoreboard_menu.set_variables(scoreboard_sentence, scoreboard_options, view, input_getter, model)

main_menu.set_variables(main_sentence, main_options, view, input_getter)

main_menu.run()



