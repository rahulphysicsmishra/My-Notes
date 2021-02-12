from collections import Counter, namedtuple, OrderedDict, deque, defaultdict

a = "aaaaaabbbbccc"
my_counter = Counter(a)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common()[2][1])
print(list(my_counter.elements()))
up_date = my_counter.update(['e','f','g','h'])
print(my_counter.items())
set_def = my_counter.setdefault('k', 4)
print(my_counter.items())



# Named tuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)



# Ordered dict eample
ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1

print(ordered_dict)


# default dict example
d = defaultdict(int)  # parameter integer means it will give a default int value when the key is not present in the dict
d['a'] = 1
d['b'] = 2
print(d['c'])  # gives defalut value zero when c is not present in the dict

e = defaultdict(float)
e['a'] = 3
e['b'] = 4
print(e['d'])  # gives 0.0 default value

f = defaultdict(list)
print(f['a'])  # it will return empty list as default value
# if f = {} , then print(f['a']) will raise key error.



# deque example

d = deque()

d.append(1)
d.append(2)
d.append(3)
d.appendleft(5)
d.extend([6,7,8])
d.extendleft([0, 9, 1.1])
print(d, type(d))
d.rotate(1)
print(d)
d.rotate(-1)
print(d)