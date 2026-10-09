'''
Ploymorphism ->Method Overloading,Method Overriding (super(),Operator Overloading (Usage of magic methods)

a = '5'
b = '6'
#if a and b are integers ->addition,a and b are strings ->contatenation,if a and b are lists ->methods
print(a+b)
print(6+7)
print([6,7]+[9,4])
#if u consider integers
a = 7; b = 8
print(a.__add__(b))
a = [1,2,4]
print(a.__add__([2,3,4])) 
print(a.__len__())#len(a)
print(a.__delitem__(2)) #del a[2]
print(a)

#now lets us understand how above dunder methods such as __add__ ,__str__
class WatchHistory:
    """We want to calculate the watchhistory of user"""
    def __init__(self,hours):
        self.hours = hours
    #here if we want to calculate the watchhistory
#a = WatchHistory(120)
a = WatchHistory(120)
b = WatchHistory(40)
#print(a+b)
print(a.hours + b.hours) #here directly we have taken integers

class WatchHistory:
    """We want to calculate the watchhistory of user"""
    def __init__(self,hours):
        self.hours = hours
    #here if we want to calculate the watchhistory
    def __add__(self,value):
        return self.hours + value.hours
#a = WatchHistory(120)
a = WatchHistory(120)
b = WatchHistory(40)
print(a+b)
#So in the above case we are overloading our dunder adad method

class WatchHistory:
    """We want to calculate the watchHistory of user"""
    def __init__(self,hours):
        self.hours = hours
    #here if we want to calculate the watchhistory
    def __add__(self,value):
        return self.hours + value.hours
    def __str__(self):
        return f"The  WatchHistory is {self.hours} hours"
a = WatchHistory(30)
b = WatchHistory(40)
print(a)
print(a+b)
'''
#Abstraction : It is one of the key feature of OOP which helps in implementing important information,
#if we want to invokoe a specific method from a base class to be applied for all derived classes
import abc
from abc import ABC,abstractmethod
#instagram -- upload photo,video,reel
class Content(ABC):
    @abstractmethod
    def upload(self):
        pass
class Photo(Content):
    def upload(self):
        print(f'Photo is Uploading')
        print(f'Compressing Photo')
        print(f'Uploaded Photo with Effects')
class Video(Content):
    def upload(self):
        print(f'Video is uploaded')
        print(f'Encoding the video')
        print(f'Video is Commpressed without lossing quality')
class Reel(Content):
    def upload(self):
        print(f'Adding Effects to the Reel')
        print(f'Uploading the reel')
        print(f'Reel is uploaded with tags')
'''contents = [Photo(),Video(),Reel()]
for content in contents:
    content.upload()'''
pcontent = Photo()
pcontent.upload()
vcontent = Video()
vcontent.upload()
rcontent = Reel()
rcontent.upload()
