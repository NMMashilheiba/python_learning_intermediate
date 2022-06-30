#Dictionary: Key-value pair, unordered, mutable
mydict = {"name": "Max", "age": 24, "city": "Newyork"}
print(mydict["name"])

mydict1 = dict(name="Mary", age=28, city= "NewYork")
print(mydict1["name"])

mydict["email"] = "max@yahoo.com"
mydict["email"] = "nicemax@yahoo.com"

del mydict["age"]
mydict.pop("name")

#val = mydict["age"]
print(mydict)
