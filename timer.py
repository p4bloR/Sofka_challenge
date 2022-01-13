
class Timer (threading.Thread):
   def __init__(self, time, message = "You ran out of time"):
      threading.Thread.__init__(self)
      self.time = time
      self.message = message

   def run(self):
       countdown = self.time
       for i in range(countdown, -1, -1):
            print(i, end='\r')
            sleep(1)
       print(self.message)
