import sys
def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()
print(g)  # it will give generator object location.....

# to get items, we can loop over it using for loop
# for i in g:
#     print(i)  # if i don't comment for loop, i cannot iterate again by using next function....

# to get item one by one
value = next(g)  # it will iter first item...
print(value)

value = next(g)  # it will call 2nd item.....
print(value)

value = next(g)  # it will give 3rd item...
print(value)  # if i use next func again, it will give stopiteration error, bcos no more items left to iterate

# i cannot call print(sum(g)) or print(sorted(g)) now, ...as i have already iterated over items


# for generator comp
my_gen_comp = (i for i in range(10) if i % 2 == 0)
# for i in my_gen_comp:
#     print(i)  # loop over to get items
print(my_gen_comp)  # gives generator obj at memory location
print(list(my_gen_comp))  # to get items in a list....
print(sys.getsizeof(my_gen_comp))  # takes less size

mylist = [i for i in range(10) if i % 2 == 0]  # using list comp
print(mylist)
print(sys.getsizeof(mylist))  # takes larger size
