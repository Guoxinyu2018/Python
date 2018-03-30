class A:
    pass
class B(A):
    pass
a=A()
print(issubclass(B,A))   #B为A的子类 返回True

class Rectangle:
    def __init__(self,x,y):
        self.x=x          #self.x为类的实例化后实例化对象的局部变量 x为传入的参数
        self.y=y
    def getperi(self):
        return(self.x+self.y)*2
    def getArea(self):
        return self.x*self.y
rect=Rectangle(3,4)
print(rect.getperi())
print(rect.getArea())
#算术运算
class Caucl(int): #继承int
    def fun(self):
        return int.__floordiv__(self,other)
    def fun2(self):
        return int.__truediv__(self,other)
aa=Caucl(3)
bb=Caucl(1)
print(aa/bb,aa//bb)   #/真除（保留小数）  //Floor除（只留整数）


