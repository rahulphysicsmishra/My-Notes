"""
The term Recursion can be defined as the process of defining something in terms of itself.
 In simple words, it is a process in which a function calls itself directly or indirectly.

Advantages of using recursion

1. A complicated function can be split down into smaller sub-problems utilizing recursion.
2. Sequence creation is simpler through recursion than utilizing any nested iteration.
3. Recursive functions render the code look simple and effective.

Disadvantages of using recursion

1. A lot of memory and time is taken through recursive calls which makes it expensive for use.
2. Recursive functions are challenging to debug.
3. The reasoning behind recursion can sometimes be tough to think through.
"""

# Program to print fibonacci series upto n terms

# Recursive function
def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return (recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2))

n_terms = 10
# check if the number of terms is valid
if n_terms <= 0:
    print("Invalid input ! Please input a +ve value")
else:
    print("Fibonacci series:")
    for i in range(n_terms):
        print(recursive_fibonacci(i))





# Recursion of a factorial
def recursive_factorial(n):
    if n == 1:
        return n
    else:
        return n * recursive_factorial(n-1)

# User input
num = int(input("Enter a number to find factorial: "))

if num < 0:
    print("Invalid input ! please enter a +ve num")
elif num == 0:
    print("Factorial of num 0 is 1")
else:
    print("factorial of num", num, "=", recursive_factorial(num))

