from functools import lru_cache

@lru_cache(maxsize=3)
def calculate(number):
    print("計算")
    return number ** 2

print(calculate(2))
print(calculate(3))
print(calculate(2))
print(calculate(4))
print(calculate(3))

print(calculate.cache_info())