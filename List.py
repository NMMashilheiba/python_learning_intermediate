#Lists: ordered, mutable, allows duplicate elements

mylist = ["banana", "apple", "kiwi"]
mylist2 = [4, 5, 1, 2, 8, 7]

print(sorted(mylist2)) 
print()
mylist2.sort()
print(mylist2)

#Slicing
new = mylist2[1:4]
print(new)
#optional step index
new = mylist2[1::2]
print(new)
#trick to reverse
new = mylist2[::-1]
print(new)
