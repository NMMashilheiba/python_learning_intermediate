from multiprocessing import Process, Value, Array, Lock
import os

def add_100(number, lock):
    for i in range(100):
        lock.acquire()
        number.value += 1
        lock.release()

if __name__ == '__main__':
    lock = Lock()
    shared_value = Value('i', 0)
    print('Shared value a beginning is', shared_value.value)

    p1 = Process(target=add_100, args=(shared_value, lock))
    p2 = Process(target=add_100, args=(shared_value, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Shared value at end is', shared_value.value)
