"""
Deque(double end queue) is the optimized list for quicker append and pop
operations from both sides of the container.

Syntax:
class collections.deque(list)
"""


# Python code to demonstrate deque

from collections import deque

# Declaring deque
queue = deque(['name', 'age', 'DOB'])
print(queue)


# Inserting elements in deque.... it can be inserted from both ends...
# appendleft() to insert from left side and append() from right side....

from collections import deque

#initializing deque
de = deque([1, 2, 3])

#using append() to insert element at right end
# insert 4 at the end of deque
de.append(4)

# printing modified deque
print("The deque after appending at right is: ")
print(de)

# using appendleft() to insert element at right end
# insert 6 at the beginning of deque
de.appendleft(6)

# printing modified deque
print("The deque after appending at left is: ")
print(de)


# Removing elements - pop() to remove from right side, popleft() to remove from left end

from collections import deque

# initializing deque
de = deque([6, 1, 2, 3, 4])

# using pop() to delete element from right end
# delete 4 from the right end of deque
de.pop()

# printing modified deque
print("The deque after deleting from right is:  ")
print(de)

# using popleft() to delete element from left end
# delete 6 from the left end of deque
de.popleft()

# printing modified deque
print("The deque after deleting from left is: ")
print(de)

