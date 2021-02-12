"""continue is opposite to that of break statement, instead of
terminating the loop, it forces to execute the next iteration of the
loop.....When the continue statement is executed in the loop,
the code inside the loop following the continue statement will
 be skipped and the next iteration of the loop will begin"""

for i in range(1, 10):

    # If i = 6, continue to next iteration
    # without printing
    if i == 6:
        continue
    else:
        # Otherwise print the value of i
        print(i, end=" ")

