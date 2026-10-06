'''
OOP ->Encapsulation -> it is one of the key features of OOP, it binds(bundle) the data (attributes) and methods (actions) around a single class.
it aslo provides specific accessibility as public,protected and private attributes.
Let's understand in details about each one in detail
Public Attributes ->These are defined inside the class and can be modified outside the class

class Users:
    """Users data"""
    def __init__(self,name):
        self.name = name #public attribute
    def details(self):
        print(f'User name is {self.name}')
u1 = Users("vishala")
u1.details()
print(u1.name)
u1.name = "swpana" #modifying public attribute
u1.details()

#Protected Attribute: This is generally preferred in Developer point of view as a hint,we generally use single underscore the attribute,they can also be modified
#outside the class.
class Users:
    """Users data"""
    def __init__(self,name,_otp):
        self.name = name#public attribute
        self._otp = _otp #protected attribute
    def details(self):
        print(f'User name is {self.name}')
u1 = Users("vishala",8745)
print(u1._otp)
u1._otp = 3425
print(u1._otp)

#Private Attribute -> In this case we make the attribute name with double leading,underscores,in very specific where the attributes need not be accesses directely
#such as we make it as __var
#python breaches it by Name Mangling,but we prefer uasage of Setters and Getters or (Accessors/Modifiers)
class Users:
    """Users data"""
    def __init__(self,name,_otp,__password):
        self.name = name#public attribute
        self._otp = _otp #protected attribute
        self.__password = __password #private attributes
    def details(self):
        print(f'User name is {self.name}')
u1 = Users("vishala",3425,"vishala@2005")
print(u1._Users__password)#here NameMnagling is used as we can access
#private attributes by classname with leading underscore usage
#As NameMangling is not recommended approach we make use of Accessors and modifiers in python

class Users:
    """Users data"""
    def __init__(self,name,_otp,__password):
        self.name = name#public attribute
        self._otp = _otp #protected attribute
        self.__password = __password #private attributes
        #To make use of private attributes (getter method)
    def get_password(self):
        #return "*******"
        return self.__password
    #Now to modify the password (setter method)
    def set_password(self,new_password):
        if len(new_password) >= 6:
            self.___password = new_password
            print("password is updated")
            return self.__password
        else:
            return "Make sure to have password with min 6 characters"
    def details(self):
        print(f'User name is {self.name}')
u1 = Users("vishala",4322,"swapna")
print(u1.get_password())
print(u1.set_password("vishala@29"))
u1.set_password("vishala@29")
print(u1.get_password())
print(u1.__dict__)
u2 =  Users("meena",4566,"meena@17")
print(u2.get_password())
u2.set_password("thanu")
print(u2.get_password())

#Inheritance ->Single Inheritance,Multiple Inheritance,Multilevel Inheritance,Hierarchiacal Inheritance,Hybrid Inheritance
#Inheritance ->It is one of the key features of OOP,which helps in acquiring or reusing the properties (attributes,methods) from one class to another classI
class Base_class: #parent class
    statements(s)...
class Derived_Class(Base_class): #Derived ->child class
    statements(s)...
    ................
#Single Inheritance -> Finger print
calss A:
    statements(s)....
class B :
    statements(s)....
    .........

#Let's take example of Social Media Login
class Users:
    """Users details"""
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    #initial case we just display
    def full_name(self):
        return self.fname + self.lname
#u1 = Users("vishala","gottapu")
#print(u1.full_name)
#class User_v1(Users):
    #pass
#u1 = User_v1("Vishala","Gottapu")
#print(u1.full_name())
class User_v2(Users):
    """Updating username"""
    def update_name(self):
        return self.fname.title().strip()+" "+self.lname.title().strip()
u1 = User_v2("vishala","  Gottapu")
print(u1.full_name())
print(u1.update_name())
'''
class Student:
    def __init__(self, name, _marks, __password):
        self.name = name              # Public attribute
        self._marks = _marks          # Protected attribute
        self.__password = __password  # Private attribute 
    def get_marks(self):
        return self._marks 
    def set_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self._marks = new_marks
            print("Marks updated")
        else:
            print("Invalid marks")  
    def get_password(self):
        return self.__password    
    def set_password(self, new_password):
        if len(new_password) >= 6:
            self.__password = new_password
            print("Password updated")
        else:
            print("Password must have at least 6 characters")
s1 = Student("Vishalakshi", 85, "student123")
print("Name:", s1.name)
print("Marks:", s1.get_marks())
s1.set_marks(90)
print("Updated Marks:", s1.get_marks())
print("Password:", s1.get_password())
s1.set_password("newpass123")
print("Updated Password:", s1.get_password())
