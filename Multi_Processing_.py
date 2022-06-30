from multiprocessing import Process
import time
import os

start = time.perf_counter()

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)



if __name__ == '__main__':

    start = time.perf_counter()

    processes = []
    num_processes = os.cpu_count()

    for i in range(num_processes):
        p = Process(target=square_numbers)
        processes.append(p)

    for p in processes:
        p.start()

    for p in processes:
        p.join()
    # for p in processes:
    #     print(p)

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} seconds')
    

