class A:
    def hello(self):
        print("Hello from class A")

class B:
    def hello(self):
        print("Hello from class B")

class C(A,B):
    pass

obj = C()

obj.hello()  
print(C.mro())