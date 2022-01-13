from inputgetter import InputGetter
from inputimeout import inputimeout, TimeoutOccurred

from threading import Thread
from time import sleep
import sys
#from timer import Timer


class TimeOutGetter(InputGetter):

    def __init__(self):
        self.looping_condition = True
        self.output_condition = False
        self.input = None


    def get_input(self, time):
        t1 = Thread(target=self.timer, args=(time, self.looping_condition))
        t1.start()
        t2 = Thread(target=self.get_inputimeout, args=(time, self.input))
        t2.start()
        t1.join()
        t2.join()
        if self.output_condition:
            return self.input
        else:
            return False

    def get_inputimeout(self, time, input, message = "You ran out of time"):
        try:
            input = inputimeout(prompt='', timeout=time)
            self.looping_condition = False
            self.input = input
            self.output_condition = True
        except TimeoutOccurred:
            print(message)
            return False

    def timer(self, time, looping_condition):
        countdown = time
        for i in range(countdown, -1, -1):
            print("time remaining",i, end='\r')
            sleep(1)   #waits 45 seconds
            if not self.looping_condition:
                break







