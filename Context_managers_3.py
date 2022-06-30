from contextlib import contextmanager

@contextmanager
def open_managed_file(filemane):
    file = open(filemane, 'w')
    print('enter def 1st:')
    try:
        print('enter try block:')
        yield file
    except Exception as e:
        print('enter exception block:')
        print('Execption:', e)
    finally:
        file.close()
        print('file closed')

with open_managed_file('context_manage_def.txt') as f:
    f.write('writing on file context_manage_def...')
    #f.opennn()
print('...completed')

