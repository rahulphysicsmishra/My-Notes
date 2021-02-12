"""function which is also known as a subroutine, procedure, subprocess etc. A function is a sequence of instructions packed as a unit to perform a certain
 task. When the logic of a complex function is divided into several self-contained steps that are themselves functions, then these functions are called
 helper functions or subroutines.

Subroutines in Python are called by main function which is responsible for coordination the use of these subroutines. Subroutines have single entry point.

Coroutines are generalization of subroutines. They are used for cooperative multitasking where a process voluntarily yield (give away) control periodically
 or when idle in order to enable multiple applications to be run simultaneously. The difference between coroutine and subroutine is :

Unlike subroutines, coroutines have many entry points for suspending and resuming execution. Coroutine can suspend its execution and transfer control to
other coroutine and can resume again execution from the point it left off.

Unlike subroutines, there is no main function to call coroutines in particular order and coordinate the results. Coroutines are cooperative that
 means they link together to form a pipeline. One coroutine may consume input data and send it to other which process it. Finally there may be a
 coroutine to display result.

yield can also be used as expression. For example on the right side of the assignment –

line = (yield)
whatever value we send to coroutine is captured and returned by (yield) expression.
A value can be send to the coroutine by send() method"""


def print_name(prefix):
    print("Searching prefix: {}".format(prefix))
    while True:
        name = yield
        if prefix in name:
            print(name)

# calling coroutine, nothing will happen
corou = print_name("Dear")

# This will start execution of coroutine and
#prints first line "Searching prefix" and advance
# execution to the first yield expression
corou.__next__()

# sending inputs
corou.send("hari")
corou.send("Dear narayan")

# Execution of coroutine is similar to the generator. When we call coroutine nothing happens, it runs only in response to the next()
# and send() method. This can be seen clearly in above example, as only after calling __next__() method, out coroutine starts executing.
# After this call, execution advances to the first yield expression, now execution pauses and wait for value to be sent to corou object.
# When first value is sent to it, it checks for prefix and print name if prefix present. After printing name it goes through loop until
# it encounters name = (yield) expression again.