# custom context manager
class ManageFile:
    def __init__(self, filename):
        print('__init__')
        self.filename = filename
    
    def __enter__(self):
        print('__enter__')
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        print('__exit__')

with ManageFile('Custom_context_manager.txt') as file:
    print('do some stuff...')
    file.write('writing on file...')