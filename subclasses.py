#Threading using subclasses
import threading
import time

class myThread(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID

    def run(self):
        print ("Starting " + self.threadID)
        i = 0
        while i >= 0:
            i = i + 1
        print i
        print ("Exiting " + self.threadID)

t1 = myThread('1')
t2 = myThread('2')
t1.start()
t2.start()
t1.join()
t2.join()
