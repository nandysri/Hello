import time
import random

class Times:
      def __init__(self):
              self.start_time = time.time()
      def duration(self):
            return time.time() - self.start_time

nandu =Times()
                 


print('Finished in {} seconds nandu.'.format(nandu.duration()))
