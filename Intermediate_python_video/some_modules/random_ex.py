import random

a = random.random()
print(a)
a1 = random.uniform(1,3)
print(a1)
a2 = random.randint(2, 5)  # it includes 5 also.... use randrange for not including upper bound
print(a2)
a3 = random.randrange(2, 5)  #exclude 5, the upper bound
print(a3)
a4 = random.normalvariate(0, 1)  # for statistical mu and sigma usage
print(a4)

mylist = list("ABCDEFGH")
print(mylist)
a5 = random.choice(mylist)
print(a5)
a6 = random.sample(mylist, 3)
print(a6)
a7 = random.choices(mylist, k=3)
print(a7)
random.shuffle(mylist)
print(mylist)



