# Tuple: ordered, immutable, allows duplicate elements

mytuple = "Max", 23, "NewYork"
#print(mytuple) 

SingleTuple = "Max",
#print(type(SingleTuple))

#using tuple() 
mytuple1 = tuple(["Max", 23, "NewYork"])
#print(mytuple1)
#print(type(mytuple1))

if "NewYork" in mytuple:
    print("Yes")
else:
    print("No")

