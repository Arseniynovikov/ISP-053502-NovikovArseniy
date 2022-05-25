def dec(func):
    def take_docstring():
        print(func.__doc__)

@dec
def super():
    "this is my docstring"


