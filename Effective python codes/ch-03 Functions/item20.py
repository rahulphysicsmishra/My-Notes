#  In the case of dividing by zero,
# returning None seems natural because
# the result is undefined:
def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

x, y = 1, 0
result = careful_divide(x, y)
if result is None:
    print('Invalid inputs')

#. You might accidentally look for any False-equivalent
# value to indicate errors instead of only looking for None
c, d = 0, 1
result1 = careful_divide(c, d) # it returns 0 so the if block should not run
if not result1:
    print('Invalid inputs') # It should not run but it runs

# Two ways to reduce such error
# 1. split the return value into 2 tuple
def careful_divide1(x, y):
    try:
        return True, x / y
    except ZeroDivisionError:
        return False, None

success, result2 = careful_divide1(c, d)
if not success:
    print('Invalid inputs')
else:
    print('Success')

# 2nd way is to never return None for special cases.
def careful_divide2(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs')

x1, y1 = 5, 2
try:
    result3 = careful_divide2(x1, y1)
except ValueError:
    print('Invalid inputs')
else:
    print('result is %.1f' %result3)