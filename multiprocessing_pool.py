import multiprocessing
import multiprocessing.pool



class NoDaemonProcess(multiprocessing.Process):
    def _get_daemon(self):
        return False

    def _set_daemon(self, value):
        pass
    daemon = property(_get_daemon, _set_daemon)
# ==============================================


class MyPool(multiprocessing.pool.Pool):
    Process = NoDaemonProcess

def Print_Pool(id1,id2):
    print(id1,id2,"\t",multiprocessing.current_process().name)


def pool_Start(id):
    Pool = MyPool()
    for i in range(id):
        Pool.apply_async(Print_Pool, args=(id,i))
    Pool.close()
    Pool.join()

def main():
    Pool = MyPool()
    for i in range(10): # creating a pool with 10 arguements for testing purposes
        Pool.apply_async(pool_Start, args=(i,)) # applying threads to the current pool
    Pool.close()
    Pool.join()


if __name__ == "__main__":
    main()