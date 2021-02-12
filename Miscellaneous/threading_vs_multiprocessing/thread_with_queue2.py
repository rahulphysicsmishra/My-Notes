from threading import Thread, Lock, current_thread
from queue import Queue
import time

def worker(q):
    while True:
        value = q.get()

        #processing...
        print(f'in {current_thread().name} got {value}')
        q.task_done()

if __name__ == "__main__":

    q = Queue()

    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q,))
        thread.daemon = True
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()

    print('end main')
