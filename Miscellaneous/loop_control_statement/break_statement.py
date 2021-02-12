"""A condition where you want to exit the loop completely,
skip an iteration or ignore that condition...These can be done
by loop control statements...

Break:-

It is used to terminate the loop or statement in which it is
 present. After that, the control will pass to the statements
 that are present after the break statement, if available.
 If the break statement is present in the nested loop, then it
 terminates only those loops which contain break statement.."""

s = 'Hari ki maya'
for letter in s:

    print(letter)
    # break the loop as soon as it sees 'k'
    if letter == 'k':
        break

print('Out of for loop')
print()

i = 0

# Using while loop
while True:

    print(s[i])
    if s[i] == 'k':
        break
    i += 1

print('Out of while loop')
