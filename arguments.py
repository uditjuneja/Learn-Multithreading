import threading


def some_func(one, two, an_arg = None):
    global my_var
    my_var += one + two
    an_arg.append(my_var)


my_var = 0
my_list = []
eg = threading.Thread(target=some_func,
                      args = (1, 2),
                      kwargs = {"an_arg": my_list})
eg.start()
eg.join()
my_var
my_list

