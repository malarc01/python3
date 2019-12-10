message = "a"


def greet(name):
    global message
    message = "b"


greet("Monkey")
print(message)
