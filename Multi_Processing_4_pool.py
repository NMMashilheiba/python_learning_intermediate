from multiprocessing import Pool, pool
from multiprocessing.context import Process
import time

def cube(number):
    #time.sleep(5)
    return number * number * number

if __name__ == '__main__':

    numbers = range(10)
    pool = Pool()

    #map, apply, join, close
    result = pool.map(cube, numbers)
    #result = pool.apply(cube, numbers[2: 3])

    pool.close()

    pool.join()

    print(result)
