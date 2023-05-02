import math

class Circle:
    def __init__(self):
        self.a=0
        self.u=0


    def getArea(self,r):
        self.a=math.pi*r*r
        return self.a


    def getCircumference(self,r):
        self.u=2*math.pi*r
    

c=Circle()
c.getArea(float(input("Enter the radius:")))
print("Area:",c.a)
c.getCircumference(float(input("Enter the radius:")))
print("Circumference:",c.u)
