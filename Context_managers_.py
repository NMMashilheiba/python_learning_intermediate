# with context manager
with open('context_manager.txt', 'w') as file:
    file.write('Writing on file...')

# without context manager
# file = open('context_manager_.txt', 'w')
# try:
#     file.write('Writing on file...')
# finally:
#     file.close()
