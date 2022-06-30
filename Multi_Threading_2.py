# queues
from threading import Thread, Lock, current_thread
from queue import Queue
import time 

def worker(q, lock):
    while True:
        value = q.get()
        #processing...
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()

if __name__ == '__main__':
    q = Queue()
    num_threads = 5
    lock = Lock()

    for i in range(1, 11):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True
        thread.start()

    for i in range(1, 11):
        q.put(i)
    
    q.join()

    print('end main')
