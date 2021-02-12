class CountCalls:
    def __init__(self, func):
        self.func = func
        self._num_calls = 0

    def __call__(self, *args, **kwargs):
        self._num_calls += 1
        print(f'This is executed {self._num_calls} times')
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print('Hello')

say_hello()
say_hello()