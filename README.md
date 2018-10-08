Multithreading in Python is achieved using the **threading** module which provides a very simple and intuitive API for spawning multiple threads.

## Background on Multithreading
Multithreading is a way off achieving multitasking, using the concept of **threads**.

A *thread* is an entity, the smallest unit of processing that can be performed in an operating system, within a process that can be scheduled for execution.
Multiple threads can exist within one process where:
* Each thread contains its own register set and local variables (stored in a stack) 
* All thread of a process share global variables (stored in heap) and the program code

Consider the below diagrams:
### Relationship between process & thread
![alt text][relationship]

### How multiple threads exist in memory
![alt text][multiple]

### A simple example to illustrate
Consider the below example to illustrate the concept

```
import threading 
  
def print_cube(num): 
    """ 
    function to print cube of given num 
    """
    print("Cube: {}".format(num * num * num)) 
  
def print_square(num): 
    """ 
    function to print square of given num 
    """
    print("Square: {}".format(num * num)) 
  
if __name__ == "__main__": 
    # creating thread 
    t1 = threading.Thread(target=print_square, args=(10,)) 
    t2 = threading.Thread(target=print_cube, args=(10,)) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
  
    # both threads completely executed 
    print("Done!")
```
How the above process/program runs is illustrated using below diagram
![alt text][program]


[relationship]: https://cdncontribute.geeksforgeeks.org/wp-content/uploads/multithreading-python-11.png "Relationship betwen process and thread"
[multiple]: https://cdncontribute.geeksforgeeks.org/wp-content/uploads/multithreading-python-21.png "How multiple threads exist in memory"
[program]: https://cdncontribute.geeksforgeeks.org/wp-content/uploads/multithreading-python-4.png "How program with multithreading works"
