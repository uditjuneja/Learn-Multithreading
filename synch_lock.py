#Using thread synchronization lock
share_lock = 0
share_no_lock = 0
COUNT = 10000
shared_lock = threading.Lock()

def inc_with_lock():
    global share_lock
    for i in range(COUNT):
        shared_lock.acquire()
        share_lock += 1
        shared_lock.release()

def dec_with_lock():
    global share_lock
    for i in range(COUNT):
        shared_lock.acquire()
        share_lock -= 1
        shared_lock.release()

def inc_without_lock():
    global share_no_lock
    for i in range(COUNT):
        share_no_lock += 1

def dec_without_lock():
    global share_no_lock
    for i in range(COUNT):
        share_no_lock -= 1

if __name__ == '__main__':
    t1 = threading.Thread(target=inc_with_lock)
    t2 = threading.Thread(target=dec_with_lock)
    t3 = threading.Thread(target=inc_without_lock)
    t4 = threading.Thread(target=dec_without_lock)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print share_lock
    print share_no_lock
