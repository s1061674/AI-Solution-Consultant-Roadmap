class Resource:
    def __enter__(self):
        print("開始")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print("結束")

        return True

with Resource() as resource:
    print("執行中")
    10 / 0

print("程式繼續")