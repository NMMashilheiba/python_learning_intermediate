try:
    a = 5 / 1
    b = a + 2
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("Everything is fine")
finally:
    print('cleaning up...')