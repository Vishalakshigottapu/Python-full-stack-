'''
Scope of variables:
1.local variable
->A variable is define inside the function call it as local variable, where the variables can only access with in that function
eg:
def display():
    name = 'vishala'
    print(name)
display()
2.global variable
->A variable that is defined outside the functio call and it can access anywhere throught out the program
#Global keyword:
Global keyword used to reaccess new values to variable that was already define outside yhe function call
eg:
a = 90
print(a)
def display():
    global a
    a = 10
display()
print(a)
Passing by value:
def even_odd(num)
    if num % 2 == 0:
        print(f'{num} is even')
    else::
        print(f'{num} is odd')
even_odd(109)

passing by refrenece:
num = 5
def even_odd(num):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
even_odd(num)

Recursive function:
->The function call itself untill the base condition met
eg:
'''
def fac(a):
    if a == 0 or a == 1:
        return a
    return a * fac(a-1)
print(fac(6))






