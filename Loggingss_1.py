import logging
import logging.config
#import os
#from os import path
#cwd = os.getcwd()
#print(cwd)

#log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')

#logging.config.fileConfig(log_file_path)
logging.config.fileConfig('C:\\Users\\ningt\\Python_Intermediate\\logging.conf')

logger = logging.getLogger('simpleExample')
logger.debug('this is a debug message')


