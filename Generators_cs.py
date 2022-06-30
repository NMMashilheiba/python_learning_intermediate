def square_num(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

def square_num_generator(nums):
    for i in nums:
        yield(i*i)   

#using list comprehension
# my_nums = [x*x for x in [1, 2, 3, 4, 5]]

#generator expression
my_nums = (x*x for x in [1, 2, 3, 4, 5])
print(my_nums)

#my_nums = square_num_generator([1, 2, 3, 4, 5])

for num in my_nums:
    print (num)

# print (next(my_nums))
# print (next(my_nums))
# print (next(my_nums))
# print (next(my_nums))
# print (next(my_nums))