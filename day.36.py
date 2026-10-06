'''
Functions -> User Defined functions,built-in functions, anonymous functions(lambda keyword),recursive function
Anonymous functions -> Nameless functions (helper functions), we define them by using lambda keyword
syntax:lambda arg(s): expression

def cal_area(l,b):
    """Area of rectangle"""
    return l*b
print(cal_area(7,4))

#Same using anonymous function
area = lambda l,b : l*b
print(area(7,4))

#find the area of square with side value as 5
area = lambda side : side**2
print(area(5))

#find the area of triangle
area = lambda b,h : 1/2(b*h)
print(area(9,4))


#Social media user first name last name -> full name
fname,lname = input('enter the names:').split(',')
#print(fname,lname)
full_name = lambda fname,lname : fname.title().strip()+" "+lname.title().strip()
print(full_name(fname,lname))

#accepting input from user and find even or odd
n = int(input('enter a number:'))
result = lambda n : 'even' if n%2==0 else 'odd'
result1 = lambda n : n**2 if n%2==0 else n**3
print(result(n))
print('new result is ',result1(n))

names = ['codegnan','python','vishala','pfs','java']
g = lambda x:x in names
h = lambda x: len(x) in names
o = lambda x: len(x)
print(g('python'))
print(h('codegnan'))
print(o('vishala'))

#filter(),map(),reduce()
#filter()-> we want to specific filtered result
data = [1,3,4,5,24,12,36,3]
#filter only even numbers from list
new_data = list(filter(lambda x:x%2==0,data))
print(new_data)

#try above using user defined function with a for loop..
def filter_even_numbers(input_list):
    even_numbers = []
    for num in input_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

#filter desired names from the list
names = ['vishala','python','ampolu','bachi','kick']
new_names =list(filter(lambda i:len(i) >=6,names))
print(new_names)


#map() -> it will apply logic for each value (google maps)
lst = list(map(int,input('enter the values:').split(',')))
print(lst)
data = [1,3,5,7,-23]
final = list(map(lambda x,y:x+y, lst, data))#it automatically maps the length
print(final)

prices = [2000,2500,1500,4500,3000]
#discount of 10% for every price
disc_prices = list(map(lambda price:(price - price *0.1),prices))
print(disc_prices)


#reduce -> functools
#reduce -> it will check for logic and make it to a single vales
import functools
from functools import reduce
result = reduce(lambda x,y:x*y,[12,3,4,5,6])
print(result)
f = reduce(lambda x,y:x*y,[12,3,4,5,6])
print(f)

#Recursive Functions : a function can call itself
#Factorial,Fibonacci,sum of numbers...
#Recursive Functions ->Basecase (it tells when to stop the recursion)
#                     ->Recursive case(it tells how to start recursion)


def func():
    """docsring"""
    if base: #base case
        return
func()

def test():
    """testing"""
    return test() #we missed out base case
print(test())
'''
#let's link above case to factorial
#5!-->5*(5-4)*(5-3)*(5-2)*(5-1)*1
n = int(input('enter the value:'))
def fact(n):
    """Factorial"""
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "input must be greater than 1"
    else:
        return n * fact(n-1)
print(fact(n))
    


