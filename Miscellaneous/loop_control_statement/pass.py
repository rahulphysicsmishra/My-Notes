"""Pass statement does nothing. It is used when a statement
is required syntactically but you do not want any command or code
to execute.. It is like a null operation... pass is also used
as empty control statement, function and classes.."""

s = 'geeks'

# Empty loop
for i in s:
    pass  # No errors will be raised

# Empty function
def fun():
    pass

# No error will be raised
fun()

# Pass statement
for i in s:
    if i == 'k':
        print('Pass executed')
        pass
    print(i)
