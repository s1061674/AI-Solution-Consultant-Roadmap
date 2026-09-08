from contextlib import contextmanager

@contextmanager
def connection():
    print("連線開啟")

    try:
        yield "DATABASE"
    finally:
        print("連線關閉")

with connection() as db:
    10/0
    print(db)
    