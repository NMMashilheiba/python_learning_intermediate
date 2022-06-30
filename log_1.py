import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('C:\\Users\\ningt\Python_Intermediate\\logs\\employe_its_log.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

#logging.basicConfig(filename='C:\\Users\\ningt\Python Intermediate\\logs\\employe_log.log', level=logging.INFO, 
#                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('Created employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@yahoo.com'.format(self.first, self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Anna', 'Smith')
emp_2 = Employee('Tina', 'Smith')
emp_2 = Employee('Tobey', 'Spidey')