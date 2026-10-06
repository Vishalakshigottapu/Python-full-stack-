
OOP->Object Orirnted Programming ->It is a principle or paradigm which revolves around objects.
->It is a principle which make the program too work with objects not only functions.

It has two concepts or object contains:
->Attributes (data) ->Properties or Characteristics of an object
->Methods(behaviour) ->It performs the actions for the objects

An Objects a real world entity,where as class is a blueprint of an objects.
Syntax -> class is the keyword
class ClassName:                           class ClassName:
    """Doc string"""                            """Doc string"""
    #Attributes (characteristics)             def __init__(self,attrs):
    .................                 (or)        ..............
    .................                             ..............

    #Methods (behaviour)                      def method(self):
    def method(self):                             statements(s).....
        ............                              ......................
        statements(s):                             
        ............

a = ClassName()
b = ClassName()

#OOP ->Encapsulation,Inheritance,Polymorphism,Abstraction
#Encapsulation-> It is one of the key properties of OOP,which bundles.
#the data including attributes and methods into a single class.
#it provides accessibility (Public,Private,Protected)
#Students Class with basic details
class Students:
    """Students class with basic details"""
    #Attributes
    name = "meenakshi"
    age = 19
    location = "vzm"
    #Behaviour(Action)
    def details(self):
        print(f'{self.name} is {self.age} years old and is  in {self.location}')
s1 = Students()
print(dir(s1))
print(s1.age,s1.name,s1.location)
s1.details()
print(s1.__class__)#returns class name (__class__) -->dunder class
print(s1.__doc__)#returns doc strings
print(s1.__dict__)#returns empty as we didn't have constructor (method)
#whatever objects we creats its only same
s2 = Students()
s2.name = "vishalakshi"
s2.age = 22
s2.location = "vizag"
s2.details()


#In the above case we want to modify the attributes such that we can create multiple objects with specific attributed and methods
class Students:
    """Students class with Actions"""
    def profile(self,name,age,email_id,mobile):
        self.name = name
        self.age = age
        self.email = email_id
        self.phone = mobile
    #To display the details
    def display(self):
        print(f'Students name is {self.name}')
        print(f'Students email id is {self.email} and age is {self.age}')
s1 = Students()
s1.profile("swapna",21,"ampoluswapna22@gmail.com",7396260191)
s1.display()
print(s1.__dict__)
s2 = Students()
s2.profile("kick",22,"kick@gmail.com",9908831292)
s2.display()

class Students:
    def __init__(self,name,age,email_id,mobile):
        self.name = name
        self.age = age
        self.email = email_id
        self.phone = mobile
    #To display the details
    def display(self):
        print(f'Students name is {self.name}')
        print(f'Students email id is {self.email} and age is {self.age}')
s1 =Students("bhasker",23,"bhaskerswapna@gmail.com",8790055612)
s1.display()
print(s1.__dict__)
s2 = Students("thanu",11,"thanusya@gmail.com",9492019567)
s2.display()
print(s2.__dict__)
'''
#Task ->Create a Cars class with attributes as brand,color,price
class Cars:
    """Cars details"""
    brand = "Thar"
    color = "black"
    price = 2400000
    def details(self):
        print(f'brand is {self.brand} color is {self.color} is price {self.price} ')
c1 = Cars()
c1.details()
c2 = Cars()
c2.brand = "Innovo"
c2.color = "white"
c2.price = 2500000
c2.details()

