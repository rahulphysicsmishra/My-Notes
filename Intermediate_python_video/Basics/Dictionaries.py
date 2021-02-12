# Dictionary: unordered, mutable, key-value pair...no key repetition

mydict = {"name": "Max", "age": 28, "city": "New-york"}  # Method 1 to make dict
print(mydict)

print(mydict["name"])  # accessing values
print(mydict["age"])
mydict["occupation"] = "Teacher"  # How to add new key-values
print(mydict)
popped = mydict.popitem()
print(popped, type(popped))
print(mydict)
popped2 = mydict.pop('name')
print(popped2, type(popped2))
print(mydict)



mydict2 = dict(name="Mary", age= 27, city = "Boston")  # Method 2 to make dict
print(mydict2)
for key, value in mydict2.items():  # or for keys, for key in mydict.keys()
    print(key, value)  # for value, for value in mydict.values()

# to copy dict
new_dict = mydict2.copy()  # or use dict(mydict2)
new_dict['bhakt'] = "Hari naam"
print(new_dict)
print(mydict2)

# Update method
dic1 = new_dict.copy()
dic2 = {'bhakti': 'Marg', 'yog': 'hathamarg'}
dic1.update(dic2)
print(dic1)

# Tuples as key possible bcos they are immutable and lists are not..so lists as key not possible
tuple = (2,4)
dic3 = {tuple: 4}
print(dic3)

