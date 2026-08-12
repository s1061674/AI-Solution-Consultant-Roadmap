class Base:
    def hello(self):
        print("Base")


class A(Base):
    def hello(self):
        print("A")
        super().hello()


class B(Base):
    def hello(self):
        print("B")
        super().hello()


class C(A, B):
    def hello(self):
        print("C")
        super().hello()

obj = C()

obj.hello()

print(C.mro())