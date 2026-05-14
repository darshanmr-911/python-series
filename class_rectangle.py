class rectangle:
    def __init__(self,lenth,width):
        self.lenth=lenth
        self.width=width
    def area(self):
        return self.lenth*self.width
    def perimeter(self):
        return 2*(self.lenth+self.width)
lenth=4
width=2
r1=rectangle(lenth,width)
print("Area of the rectangle:",r1.area())
print("Perimeter of the rectangle:",r1.perimeter())