#using process pool executor
import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} seconds...') 
    time.sleep(seconds)
    return f'Done sleeping... {seconds} '

if __name__ == '__main__':

    with concurrent.futures.ProcessPoolExecutor() as executor:
        #f1 = executor.submit(do_something, 1)
        #print(f1.result())
        seconds = [10, 2, 3, 4]

        results = [executor.submit(do_something, sec) for sec in seconds]
        for f in concurrent.futures.as_completed(results):
            print(f.result())

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')
