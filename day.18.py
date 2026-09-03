'''
Lambda Function
-> Lambda function is small anonymous function
-> Lambda can be take n number arguments, but only with one expression
->The function is defined by using lambda keyword
syntax:
lambda arguments : expression
eg:
add_ =lambda a,b,c :a+b+c
print(add_(10,20,30))

#even or odd in one line
even = lambda num : num % 2 == 0
print(even(7))

# b/w two number which one is big 
great = lambda a,b : a if a>b else b
print(great(12,34))

#cube value
cube = lambda a : a ** 3 
print(cube(2))

#Filter()
-> filter() function will perfrom only on selected elements of iterables
syntax :
filter(lambda arguments : expression, iterable)
eg:
nums = [1,2,3,4,56,67]
data_ = filter(lambda a : a%2==0,nums)
print(list(data_))


map()
->map() function will perform on all elements of a iterable
syntax:
map(lambda arguments : expression, iterable)
eg:
nums = [1,2,3,4,56,67]
get = map(lambda a : a+6,nums)
print(list(get))
#
nums = [1,2,3,4,56,67]
data_ = map(lambda a : a%2==0,nums)
print(list(data_))

reduce()
-> the reduce() function repeatly applies a functionn to the elements and reduces them to one final value.
-> it is available in the functools module.
syntax:
reduce(lambda arguments : expression, iterable)
eg:
from functools import reduce
nums = [1,2,3,4,5]
data = reduce(lambda a,b: a+b, range(1,10))
print(data)














