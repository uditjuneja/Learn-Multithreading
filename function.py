# name, target, args
# start, join, currentThread(),getName()
import threading
import time

def function(i):
    print i
    print threading.currentThread().getName()
    return

i = 1
t1 = threading.Thread(target=function, args=(i,))
t1.start()
t1.join()

t2 = threading.Thread(name="t2",target=function, args=(i,))
t2.start()
t2.join()
