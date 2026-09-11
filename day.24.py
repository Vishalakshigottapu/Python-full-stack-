'''
Exception Handling:
>This is the way handling error.
>we can write any number exception for one code written at try block.
1.try
>the try block,where we can write code which may contain error.
syntax:
try:
    code lines
2.except
>this will handle error that are raised at try block.
>syntax:
except ErrorName:
    print("ErrorName")
eg:
try:
    print(5/0)
    print(num)
except ZeroDivisionError:
    print('Division by zero')
except NameError:
    print('NameError')
    
3.else
>the else block will only execute, if no error at try block.
eg:
try:
    print('hello')
except ZeroDivisionError:
    print('Division by zero')
except NameError:
    print('NameError')
else:
    print('hello')

4.finally
>This block will execute regardless with the error at the try block
eg:
try:
    print(5/0)
    print(num)
except ZeroDivisionError:
    print('Division by zero')
except NameError:
    print('NameError')
else:
    print('No Error')
finally:
    print('End')

FileHandling
Eg:
with open('ATM PROJECT.txt','r') as file:
    print(file.read())
eg:
with open('ATM PROJECT.txt','w') as file:
    print('this is vishalakshi,i am learning python')

eg:
with open('ATM PROJECT.txt','a') as file:
    file.write('this is vishalakshi,i am learning python')
'''
with open('ATM PROJECT.txt','x') as file:
    file.write('this is vishalakshi,i am learning python')
    

    
