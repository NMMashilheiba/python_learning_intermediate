from functools import wraps

def my_logger(original_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_func.__name__), format='%(asctime)s:%(levelname)s:%(name)s:%(message)s', level=logging.INFO)

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return original_func(*args, **kwargs)
    return wrapper

def my_timer(original_func):
    import time

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_func(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in: {} sec".format(original_func.__name__, t2))
        return result
    return wrapper

import time

@my_timer
@my_logger
def display_info(name, age):
    time.sleep(2)
    print("display_info ran with arguments ({}, {})".format(name, age))

display_info("Roses", 21)