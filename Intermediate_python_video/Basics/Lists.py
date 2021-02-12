# Lists: ordered, mutable and allow duplicate elements

mylist = ['banana', 'cherry', 'apple','mango']
mylist.append('prunes')
print(mylist)
mylist.insert(1, 'pineapple')
print(mylist)
mylist.extend(['oranges','berries'])
print(mylist)
popped = mylist.pop(2)
print(mylist)
print(popped)
mylist.remove('apple')
print(mylist)
mylist.reverse()
print(mylist)
new_list = sorted(mylist)  # This method will create new list... to avoid new list, use mylist.sort()
print(new_list)
new_list.clear()
print(mylist)
print(new_list)

# some tricks
list1 = [0] * 5
print(list1)
list2 = [1,2,3,4,5]
print(list2)
print(list1 + list2)

# 3 ways of copy method

lst = [1,2,3,4,5]
lst_copy1 = list(lst)
lst_copy1.append(6)
print(lst, lst_copy1)  # append element only in lst_copy1.... it means copying successful

lst_copy2 = lst.copy()
lst_copy2.append(7)
print(lst, lst_copy2)  # append element only in lst_copy2...

lst_copy3 = lst[:]
lst_copy3.append(8)
print(lst, lst_copy3)  # append element only in lst_copy3

# list comprehension ex
list_num = [1,2,3,4,5,6]
sq_list = [i*i for i in list_num]
even_list = [i for i in list_num if i%2==0]

print(list_num, sq_list, even_list)

