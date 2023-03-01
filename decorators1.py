'''def simple_hello():
    print("Hello from simple function!")


def simple_decorator(function):
    print('We are about to call "{}"'.format(function.__name__))
    return function

decorated = simple_decorator(simple_hello)
decorated()'''

def simple_decorator(function):
    print('We are about to call "{}"'.format(function.__name__))
    return function


@simple_decorator
def simple_hello():
    print("Hello from simple function!")


simple_hello()