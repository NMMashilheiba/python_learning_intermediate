# sharing data
from threading import Thread, Lock
import time 
database_value = 0

def increase(lock):
    global database_value

    with lock:                               #context manager    
        #lock.acquire()
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy
        #lock.release()
if __name__ == '__main__':

    lock = Lock()
    print('start value', database_value)

    thread_1 = Thread(target=increase, args=(lock,))
    thread_2 = Thread(target=increase, args=(lock,))

    thread_1.start()
    thread_2.start()
    
    thread_1.join()
    thread_2.join()

    print('end value', database_value)

    print("End main")