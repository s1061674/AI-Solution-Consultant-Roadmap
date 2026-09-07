class Resource:
    def __enter__(self):
        print("資源開啟")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("資源關閉")

with Resource() as resource:
    print("使用資源")   