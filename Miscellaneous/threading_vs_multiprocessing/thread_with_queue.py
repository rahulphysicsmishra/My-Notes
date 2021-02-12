from threading import Thread, Lock
from queue import Queue
import time


if __name__ == "__main__":

    q = Queue()

    q.put(1)
    q.put(2)
    q.put(3)

    # 3 2 1 -->
    first = q.get()
    print(first)


    q.task_done()  # this tells program that we are done processing with this object
# Use print(q.empty()) to check whether queue is empty
#     q.join()
    print('end main')

# q.join()  - block the main thread until all the elements in our queue are processed