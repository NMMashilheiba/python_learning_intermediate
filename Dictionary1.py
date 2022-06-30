mydict = dict(name="Mary", age=28, city="Newyork")

#if "name" in mydict:
#    print(mydict["name"])

#try:
#    print(mydict["lastname"])
#except:
#    print("error")

for key in mydict:      #mydict.key()
    print(key, mydict[key])
print()
for value in mydict.values():
    print(value)
print()

for key, value in mydict.items():
    print(key, value)

