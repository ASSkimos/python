def repeater(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
@repeater(3)
def say_hello():
    print("Hello!")
    return "Finished"
def fibonacci_generator(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b
list=[1,2,3,4]
new_list=list[1:-1]
fibonacci_tuple = tuple(fibonacci_generator(987))
result =(x for x in list if x not in new_list)
for i in result:
    print(i)
result1 = say_hello()

print(result1)
print(fibonacci_tuple)
print(new_list)
print(result)