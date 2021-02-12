# Showing use of zip
# Normal way when you don't know zip

names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

for index, name in enumerate(names):
    hero = heroes[index]
    print(f'{name} is actually {hero}')

# Using zip
for name, hero in zip(names, heroes):  # zip return tuples of items
    print(f'{name} is actually {hero}')

universes = ['Marvel', 'DC', 'Marvel', 'DC']
for name, hero, home in zip(names, heroes, universes):
    print(f'{name} is actually {hero} and hometown is {home}')
    print(name + " is actually " + hero + " from " + home)  # Using string concatenation

# to see how zip gives tuple of items
for value in zip(names, heroes, universes):
    print(value)

# Unpacking and ignoring values
a, b, *_, d= (1, 2, 3, 4, 5, 6)  # *_ ignores other values...without using it raise error bcos of extra values
print(a, b, d)

print('*'*100)
# class based example to show setattr(), getattr()
class Person():
    pass

person = Person()
first_key = 'hari'
first_val = 'bol'

setattr(Person, first_key, first_val)
setattr(Person, first_val, first_key)

first = getattr(person, first_key)
print(first)
print(person.hari)
print(person.bol)


# how to set attributes by dict to class person
person_info = {'First':'Rahul', 'last':'Mishra'}
for key, value in person_info.items():
    setattr(person, key, value)

print(person.last, person.First)

for key in person_info.keys():
    print(getattr(person, key))



