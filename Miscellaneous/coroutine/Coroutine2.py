"""Execution of coroutine is similar to the generator. When we call coroutine nothing happens,
it runs only in response to the next() and send() method. This can be seen clearly in above example,
as only after calling __next__() method, out coroutine starts executing. After this call, execution
advances to the first yield expression, now execution pauses and wait for value to be sent to corou object.
When first value is sent to it, it checks for prefix and print name if prefix present.
After printing name it goes through loop until it encounters name = (yield) expression again."""

def print_name(prefix):
    print("Searching prefix: {}".format(prefix))
    try:
        while True:
            name = yield
            if prefix in name:
                print(name)
    except GeneratorExit:
        print("Closing coroutine!!")

corou = print_name("Hari")
corou.__next__()
corou.send("Hari bol")
corou.send("Hari Hari bol")
corou.close()
corou.send("har")  # after calling close, send() raises error
