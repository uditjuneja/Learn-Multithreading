# Learn-Multithreading
Course on multi threading in Python

Multithreading is a way of achieving multitasking. However, most often beginners confuse multi-threading with multi-processing. 

At the core of computing in operating systems, tasks are executed either of the two ways, Processes and Threads. 

In layman terms, Process is just a program in execution. Any process has 3 basic components:
- The program itself
- The data associated with that program (variables, buffers, etc.)
- The state of the program being executed. [(State of process)](https://en.wikipedia.org/wiki/Process_state)

**Okay, But What’s multiprocessing?**
The multiprocessing library uses separate memory space, multiple CPU cores, bypasses GIL limitations in CPython, child processes are killable(ex. function calls in program) and is much easier to use. Some caveats of the module are a larger memory footprint and IPC’s a little more complicated with more overhead.


**Then, What is a Thread?**
- A thread is an entity within a process that can be scheduled for execution. Also, it is the smallest unit of processing that can be performed in an OS. 

- **In a simple way, thread is a sequence of instructions within a program that can be executed independently of other code.**

A thread contains all this information in a thread control block(TCB):
        
1. **Thread identifier**: A unique id assigned to any thread 
2. **Stack pointer**: Points to the thread's stack in the process.
3. **Program counter**: a register which stores the address of instructions correctly.
4. **Thread state**: can be running, ready, waiting, start or done.
5. **Thread's register set**: registers assigned to thread of computations.
6. **Parent process pointer**: a pointer to the process control block of the process that the thread lives on. 

Multiple threads can exists within one process where :
 - each thread contains its own register set and local variables
 - all threads of process shares the global variables and the program code.

**Finally, What is Multithreading?**
Multithreading is defined as the ability of a processor to execute multiple threads concurrently.
 
We can import threading in code by just typing 'import threading'

To create the new thread, we create an object of Thread class and it takes 'target' and 'args' as a arguments   

We can use 'start' method to start a new thread and 'join' method to stop execution of current program until the thread is complete.

