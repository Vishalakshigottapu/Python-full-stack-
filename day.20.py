'''
Modules:
-> A Module is a python file(.py) that written using function, variables,operators,etc...
eg:
import math
print(math.pow(2,3))

1.Built-in modules
-> The modules are developed by programmer and those comes with installation
eg> random,math,os,sys,date and time.
eg:1
import os
print(os.getcwd())
eg:2
import sys
print(sys.version)
print(sys.path)
eg:3
import random
print(random.randint(1000,9999))
 
#2.User-define modules:
importing specific function from the module
syntax:
from module import function
from new_file import add_
eg:
from pratices import add_
print(add_(20,23))

Using alias name:
-> calling with another name
syntax:
import module as alias name
eg:
import pratices as pt
print(pt.add_(23,23))
'''
from pratices import *
print(add_(23,24))
print(sub(25,3))

