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
        seconds = [1, 2, 3, 4]

        results = executor.map(do_something, seconds)
        for result in results:
            print(result)

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')
