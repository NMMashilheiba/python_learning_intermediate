import logging
import log_1

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('C:\\Users\\ningt\Python_Intermediate\\logs\\test_log.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

#logging.basicConfig(filename='C:\\Users\\ningt\Python Intermediate\\logs\\test_log.log', level=logging.DEBUG, 
#                    format='%(asctime)s:%(levelname)s:%(message)s')

def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y
    
num_1 = 10
num_2 = 10

add_result = add(num_1, num_2)
logger.debug('Add: {} + {} ={}'.format(num_1, num_2, add_result))

sub_result = sub(num_1, num_2)
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = mul(num_1, num_2)
logger.debug("Mul: {} * {} = {}".format(num_1, num_2, mul_result))

div_result = div(num_1, num_2)
logger.debug('Divide: {} / {} = {}'.format(num_1, num_2, div_result))
