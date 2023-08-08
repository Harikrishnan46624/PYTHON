def my_decorator(func):
    def wrapper():
        return "HELLO WORLD"
    return wrapper

@my_decorator
def my_function():
    pass

result = my_function()
print(result)