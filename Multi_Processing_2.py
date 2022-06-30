from multiprocessing import Process, Value, Array, Lock
import os

def add_100(numbers, lock):
    for i in range(100):
        for i in range(len(numbers)):
            with lock:
                #lock.acquire()
                numbers[i] += 1
                #lock.release()

if __name__ == '__main__':
    lock = Lock()
    shared_array = Array('i', [0, 100, 200, 300])
    print('Shared array at beginning is', shared_array[:])

    p1 = Process(target=add_100, args=(shared_array, lock))
    p2 = Process(target=add_100, args=(shared_array, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Shared array at end is', shared_array[:])
