'''
input formatting
integer --> int(input())

num = int(input('enter your 4 digit number'))
print(num)

Float
b = float(input("Enter any number"))
print(b)

String
q = str(input("Enter a str"))
print(q)

List
nums = list(map(int, input ('Enter some numbers:').split()))
print(nums)

Tuple
nums = tuple(map(int, input ('Enter some numbers:').split()))
print(nums)

Set
nums = set (map(int, input (' Enter some number:').split()))
print(nums)

# keyword eval
data_ = eval(input('enter: '))
print(type(data_))

Output formatting
name = 'vishala'
age = 22
print('My name is',name, 'age is',age)
print('hello!',name)
print(f' My name is {name} and i am {age} years old')

%
'''
name = 'vishala'
age = 22
print('My name is %s and Im %d years old' %(name,age))

