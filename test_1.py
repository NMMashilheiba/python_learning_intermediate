from multiprocessing import Process
import time
import os


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count()

if __name__ == '__main__':
    for i in range(num_processes):
        p = Process(target=square_numbers)
        processes.append(p)

    for p in processes:
        p.start()

    for p in processes:
        p.join()
    for p in processes:
        print(p)

    print('end main')
    

