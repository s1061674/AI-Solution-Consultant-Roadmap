from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("開始執行")

        result = func(*args, **kwargs)

        print("執行完成")
        
        return result
    
    return wrapper

@decorator
def add(a, b):
    return a + b


result = add(10, 20)
print(result)
