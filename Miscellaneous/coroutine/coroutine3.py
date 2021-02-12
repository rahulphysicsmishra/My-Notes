"""
Coroutines can be used to set pipes. We can chain together coroutines and push data through pipe using send() method. A pipe needs :

An initial source(producer) which derives the whole pipe line. Producer is usually not a coroutine, it’s just a simple method.
A sink, which is the end point of the pipe. A sink might collect all data and display it.
"""

# Python program for demonstrating coroutine chaining

def producer(sentence, next_coroutine):
    '''
    Producer which just split strings and feed it
    to pattern_filter coroutines
    '''
    tokens = sentence.split(" ")
    for token in tokens:
        next_coroutine.send(token)
    next_coroutine.close()

def pattern_filter(pattern="ing", next_coroutine=None):
    '''
    Search for pattern in received token
    and if pattern got matched, send it to
    print_token() coroutine for printing
    '''
    print("Searching for {}".format(pattern))
    try:
        while True:
            token = yield
            if pattern in token:
                next_coroutine.send(token)
    except GeneratorExit:
        print("Done with filtering!!")

def print_token():
    '''
    Act as a sink, simply print the received tokens
    '''
    print("I'm sink, i'll print tokens")
    try:
        while True:
            token = yield
            print(token)
    except GeneratorExit:
        print("Done with printing")

pt = print_token()
pt.__next__()
pf = pattern_filter(next_coroutine=pt)
pf.__next__()

sentence = "Bob is running behind a fast moving car"
producer(sentence, pf)