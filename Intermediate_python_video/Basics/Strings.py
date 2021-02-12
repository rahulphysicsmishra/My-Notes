# Strings: ordered, immutable, text representation

mystring = 'I\'m Rahul'
mystring2 = """Hello \
world"""
char = mystring2[1:5]
print(mystring)
print(mystring2)
print(char)

mystring3 = " Hello World "
mystring3 = mystring3.strip()
print(mystring3.startswith('h'))
print(mystring3.endswith('d'))
print(mystring3.find('o'))
print(mystring3.count('o'))
print(mystring3.replace('orld', 'arnavat'))
mylist = mystring3.split()
newstring = ''.join(mylist)  # join method is much faster than looping to make new string
print(mylist)
print(newstring)
print(mystring3)

# time to make a new string in .join method
from timeit import default_timer as timer
my_list = ['a'] * 5
start = timer()
new_string = ''.join(my_list)
stop = timer()
print(new_string)
print(stop-start)


# time to make the same string by loop
start = timer()
newString = ''
for i in my_list:
    newString += i
stop = timer()
print(newString)
print(stop-start)

# String formatting
var = "Hari"
var2 = 3.141562
mystring4 = "The god is {} and value of pi is {:.2f}".format(var, var2)  # Observe the decimal point for 2 digits operation
mystring5 = "The god is %s" % var
mystring6 = f"The god is {var}"
print(mystring4)
print(mystring5)
print(mystring6)

