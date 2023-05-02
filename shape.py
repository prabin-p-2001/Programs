class A:
    def side(self):
        self.s=int(input("Enter side:"))

class B(A):
    def triangle(self):
        if self.s==3:
            print("triangle")

class C(B,A):
    def rectangle(self):
        if self.s==4:
            print("rectangle")

b=C()
b.side()
b.triangle()
b.rectangle()

