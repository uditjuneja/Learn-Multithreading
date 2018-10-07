#RLock - shared resource can be release by any thread
class Box(object):
    lock = threading.Lock()
    def __init__(self):
        self.total_items = 0
    def execute(self,n):
        Box.lock.acquire()
        self.total_items += n
        Box.lock.release()
    def add(self):
        print "1"
        Box.lock.acquire()
        print "1"
        self.execute(1)
        print "1"
        Box.lock.release()
    def remove(self):
        Box.lock.acquire()
        self.execute(-1)
        Box.lock.release()

def adder(box, items):
    while items > 0:
        print "Adding one item to box"
        box.add()
        time.sleep(5)
        items -= 1

def remover(box, items):
    while items > 0:
        print "Removing one item to box"
        box.remove()
        time.sleep(5)
        print "."
        items = items - 1

if __name__ == '__main__':
    items = 5
    print "putting " + str(items) + " items in box"
    box = Box()
    t1 = threading.Thread(target=adder, args=(box,items))
    t2 = threading.Thread(target=remover, args=(box,items))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print box.total_items
