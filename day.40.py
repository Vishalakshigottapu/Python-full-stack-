'''
Inheritance -- single inheritance, multiple inheritance,multilevel inheritance
#banking scenario with single inheritance
class RBI:
    """Base class"""
    cash = 10000000 #Class variable
    #classmethod
    @classmethod
    def available_cash(cls):
        print(f'Available Cash with RBI is {cls.cash}')
u1 = RBI()
print(u1.cash)
u1.available_cash()
print(RBI.cash)
RBI.available_cash()

class SBI(RBI):
    """Derived class"""
    pass

u1 = SBI()
u1.available_cash()

class HDFC(RBI):
    """Dervied class-2"""
    cash = 5000000 #class variable
    @classmethod
    def hdfc_cash(cls):
        print(f"HDFC Cash is {cls.cash}")
        print(f"Total cash is {cls.cash+RBI.cash}")
u1 = HDFC()
print(u1.cash)
u1.available_cash()
u1.hdfc_cash()
#Task1:Convert same to Hierarchical also make use of public,private,along with classmethods, class variables usage
# Constructor overriding can be avoided by usage of super()
calling superclass constructor ->super(). __init__()
calling superclass constructo with args ->super().__init__(args)
calling superclass mathod ->super().method()
#Kid-Father Property Scanario ->Constructors Overriding,method overriding
class Father:
    """Father Property only interms in cash"""
    def __init__(self):
        self.property = 5000000
    def father_prop(self):
        print(f'Father Property is {self.property}')
#class Kid(Father):
    #pass
class Kid(Father):
    """Kid has started earning"""
    def __init__(self):
        self.property = 250000
    def Kid_prop(self):
        print(f'Kid property is {self.property}')
        print(f'Total Property is {self.property + self.property}')
#obj = Father()
#obj.father_prop()
obj = Kid()
print(obj.property)
obj.father_prop()
obj.Kid_prop()
#In above we have seen constructor overriding, as we defined constructor inthe base class


class Father:
    """Father Property only interms in cash"""
    def __init__(self):
        self.fproperty = 5000000
    def father_prop(self):
        print(f'Father Property is {self.fproperty}')
#class Kid(Father):
    #pass
class Kid(Father):
    """Kid has started earning"""
    def __init__(self):
        super().__init__() #calling superclass const
        self.kproperty = 250000
    def Kid_prop(self):
        print(f'Kid property is {self.kproperty}')
        print(f'Total Property is {self.kproperty + self.fproperty}')
obj1 = Kid()
obj1.father_prop()
obj1.Kid_prop()

class Father:
    """Father Property only interms in cash"""
    def __init__(self,prop1):
        self.fproperty = prop1
    def father_prop(self):
        print(f'Father Property is {self.fproperty}')
#class Kid(Father):
    #pass
class Kid(Father):
    """Kid has started earning"""
    def __init__(self,prop2,prop1):
        super().__init__(prop1) #calling superclass const
        self.kproperty = prop2
    def Kid_prop(self):
        print(f'Kid property is {self.kproperty}')
        print(f'Total Property is {self.kproperty + self.fproperty}')
u1 = Kid(450000,2500000)
u1.father_prop()
u1.Kid_prop()

#Method Overriding ->when we define same method same in parent class and also in child class ,it will result in method Overriding,to get rid of this we prefer->super().method()
class Square:
    """Base class"""
    def __init__(self,x):
        self.x = x
    def sarea(self):
        return f'Area of Square is {self.x**2}'
class Rectangle(Square):
    """Dericed class with constructor and method name same"""
    def __init__(self,y,x):
        super().__init__(x) #calling superclass constructor with args
        self.y = y
    def rarea(self):
        return f'Area of Rectangle is {self.x * self.y}'
a1 = Rectangle(8,7)
print(a1.rarea())
print(a1.sarea())
'''
class Square:
    """Base class"""
    def __init__(self,x):
        self.x = x
    def area(self):
        print(f'Area of Square is {self.x**2}')
class Rectangle(Square):
    """Dericed class with constructor and method name same"""
    def __init__(self,y,x):
        super().__init__(x) #calling superclass constructor with args
        self.y = y
    def area(self):
        super().area() #calling superclass method
        print(f'Area of Rectangle is {self.x * self.y}')
x,y = map(int,input("Enter the values:").split(','))
obj1 = Rectangle(y,x)
obj1.area()
