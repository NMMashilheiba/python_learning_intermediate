from threading import Thread
import time
import os

start = time.perf_counter()

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

threads = []
num_threads = 10

if __name__ == '__main__':

    start = time.perf_counter()

    for i in range(num_threads):
        p = Thread(target=square_numbers)
        threads.append(p)

    for t in threads:
        t.start()

    for t in threads:
        t.join()
   
    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} seconds')
    

