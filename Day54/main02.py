import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        elapsed = end_time - start_time
        print(f"執行時間: {elapsed:.2f} 秒")
        
        return result
    
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "完成"

result = slow_function()
print(result)