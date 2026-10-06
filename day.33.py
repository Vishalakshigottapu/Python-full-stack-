'''
Nested Loops ->Pattern
Right Angled Trinagle Pattern

for i in range(5):
    for j in range(i):
        #print(f'i = {i}, j = {j}')
        print('*',end=' ')
    print()

for i in range(5):
    for j in range(i+1):
        #print(f'i = {i}, j = {j}')
        print('*',end=' ')
    print()
Inveted Triangle Pattern
for i in range(5):
    for j in range(5-i):
        #print(f'i = {i}, j = {j}')
        print('*',end=' ')
    print()

num = 5
for i in range(1,num+1):
    for j in range(num-i):
        #print(f'i = {i}, j = {j}')
        print(' ',end='')
    for j in range(i):
        print('*',end=' ')
    print()


num = 1
for i in range(4):
    for j in range(i+1):
        #print(f'i = {i}, j = {j}')
        print(num,end=' ')
        num+=1
    print()

#3
for i in range(4):
    for j in range(i+1):
        print(chr(65 + i), end=" ")
    print()
#1
char = 65
for i in range(4):
    for j in range(i+1):
        print(chr(char), end=" ")
        char+=1
    print()

#1
num = 0
for i in range(5):
    for j in range(i+1):
        print((num+i),end=' ')
        
    print()
 
#Procedure Oriented Programming ->Functions--- A Function is a block of code that performs a specific task
#We have keyword def
#User defined functions,Buli-in Functions,Anonymous Functions,Recursive Function

Syntax:
def fname(parameters):
    """Doc String(describe your function)"""
    statement(S).....
    .....                #Body of function
    .....
    return value(S).....
fname(args) # function call


def intro():
    """intro to Functions"""
    return "Hope I Am learning","hello"
print(intro())

#Positional Arguments,Keyword Arguments,Default Arguments
#Variable length argument,keyword varible length arguments
def add(a,b):
    """simple addition function"""
    return a+b
print(add(5,7))
print(add(7,9))
print(add('vishala','swapna'))# concatenation
print(add([1,2,3],[8,9,89]))
c,d = map(int,input("enter the values:").split(','))
print(add(c,d))

#print(add(8,9,2,3)) RAISE Type Error as positional agruments didn't match
#Positional arguments ->order of arguments in function definition and function call should match
#keyword Arguments ->name of the arguments should match
def grocery(item,price):
    """key arguments usage"""
    print(f'item is {item}')
    print(f'price is {price}')
grocery("milk",35)
print(grocery(price=45,item='bread'))# it also returns none as nothing to be printed
#grocery('jam',100,2)#in this case positional arguments fails as we have 2 arguments in function definition

#Default arguments ->we can make any number of argumenta as default but we have thumbrule
#def grocery(item,price=30):
#def grocery(item='milk',price): raises Error
def grocery(item='milk',price=50):
    """key arguments usage"""
    print(f'item is {item}')
    print(f'price is {price}')
grocery("milk",35)
grocery('bread')
grocery()
#*args,**kwargs

num = 5
for i in range(1,num+1):
    for j in range(num-i):
        #print(f'i = {i}, j = {j}')
        print(' ',end='')
    for j in range(i):
        print('*',end=' ')
    print()

n = 5

# Upper part
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print()

# Lower part
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print()
    '''
n = 5

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)

