'''
Day 34 24/09/26

Scope of the variables -->scope is basically the region or area where the databis accessible

local scope ,global scope, clabal keyword,enclosing scope (non local keyword)
bilt-in scope

#local scope (local variables)------> variable(s)defined inside the function area
#accessible only

def data():
    """local scope"""
    name = "codegnan"
    return f'{name}is in vizag.'
print(data())
#print(name) raises NameError



#Global Scope --> variables defined outside the function can be accessible
#inside the function also

count = 10
def details():
    """Global scope"""
    print(f'Value of count is {count} inside the function')
    #count = count+5 raises UnboundLocalError
details()
print(f'Value of count is {count} outside the function')


count = 10 #global variable
def details():
    """Priority of local vs gloabl"""
    count = 15 #local variable
    print(f'Value of count is {count} inside the function')
    count = count + 5
details()
print(f'Value of count is {count} outside the function')

#Usage of global keyword

count = 10 #global variable
def details():
    """Usage of gloabl keyword"""
    global count
    count = count+15
    print(f'Value of count is {count} inside the function')
details()
print(f'Value of count is {count} outside the function')

#Enclosing Scope --> Nested functions

def outer():
    """nested functions"""
    count = 5
    def inner():
        """Inner function to use count variable"""
        #print(count)
        nonlocal count
        count = count *4
        print(f'Value of count is {count}')
    inner()
    print(f'Value of count is {count} outside')
outer()
#print(f'Value of count is {count} outside outer function')


#Built-in Scope ->Usage of built-in functions as variables

len = 13
print(len)
print(type(len))
print(len*2)

a = ['codegnan','python','data']
print(len(a)) #raises TypeError as we have used len() somewhere

#LEBG rule -->local,Enclosing,Built-in,Global
'''
#import this
#Built-in Functions,Anonymous Functions,Recursive Functions.

#print(dir())
#print(dir(__builtins__)) #returns the list of all built-ins (Functions,Errors)

#Every built-in datatype is a built-in function -->int,float,str,list,tuple,
#set,dict,bool

#print(bool('codegnan')) #returns boolean value (True)

#print(float(int(bool(24)))) #Functions as First class objects

#print(abs(-23)) #returns the absolute value
#None,'',0,False,[],(),{} -->treated as empty values
#all(),any()
x = [23,45,'poll']
x.append(None)
#print(x)
#print(all(x)) #all(ietrable) it needs all values in the iterable to be exists

#print(any(x)) #any(iterable it needs any one value to be present

#print(bin(12)) #bin() returns the binary value

#print(chr(67)) #returns the concerned object (char)

#print(ord('A')) #returns the ASCII value for any character,symbol

#print(),type(),len(),min(),max(),input()

#print(divmod(6,2)) #performs 6//2(quotient) --> 3 6%2(remainder) --> 0
#print(pow(4,2)) #base,exponent
print(round(5.345))
print(round(5.345,2)) #digits to be rounded off


#Tomorrow's topics
#filter(),map(),zip(),enumerate()


