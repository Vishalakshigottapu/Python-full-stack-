'''
What is program?
 program is the process of instructions given by the user or programmer to planning what to do and how to .

example:
user_en = 2000
bal_ = 10000
result = bal_-user_en
print(result)

procedural language 
  An proceduarl language is organnized mainly on functions 

example: c 
 def cal_add(a,b):
    return a + b
 a = 7
 b = 9
 any_ = cal_ad(a,b)
 print(any_)

Object-oriented programming
 object oriented programming is organized mainly on classes and object 
example: python
 num = 7 
print(type(num))

what is python?
  high level language :
   python take care about memory allocation 
example:
 num = 9
 print(type(num))
 print(id(num))

  interperter language:
    line by line execution is followed by python that is the reason we call it as interperter language
example:
 num = 9 
 print(num)
 print(type(num))
 print(id(num))

  dynamically typed language:
    No to mention the type of data passing to the variable
example:
 num = 78
 any = ['python']
 nums = [1,2]
 all_ = (1,2)
 print(type(num))
 print(type(any_))
 print(type(nums))
 print(type(all_))

Why python?
 1.more library
 2.cross-platform
 3.open-source
 4.simple syntex
Applpication:
 use in Data science
 use in machine learning
 use in AI
 use in web development
 use in DL 

It was started in early 1980s,and released in the 1991 by Guido Van Rossum
And he pick the from the most loved series called monty python 
The frist version was released in the year 1991 which is python 0.9.0 and now the version we are using 3.14

Tokens 
>Tokens are the small unit in the python.
example:
num = 'python'
print(type(num))
functions
def add(a,b):
    print(a+b)
add_(4,5)

Class
>class details:
     pass
per_1 = details

identifers
> Is a name of varible or functio or class

keywords
>keywords already saved in python for an specified reason to run.
exaples:
if
else
for
while
return
print

Literals
>literals are data types that need to be saved in varibles.
examples:
num = 90
name = 'teja'

Operator
+, -, =

Statements
>statements are the instructions give to the program.
example
num = 90
 
age = 2
if age >= 18:
   print(age)

Comments:
>Once comments are open the lines inside will never execute in python file.
1.Single line comments (#)
> it is used to comment only one line
example:
age = 20
if age >= 18: #this checks age is greater or equal
   print(age)
2.Multi line comments (''' ''', """ """)
>Uses to comment more then one line
example:
python is a language 

Varibles rules
Bad ways 
>can't use number at 1st postion
>can't use special char anywhere
>can't use space
>we can't use keywords
examples:
2num = 90
$num = 89
n um = 34
if = 21

Good ways:
>Small letters, Capital letters or (_) under
example:
nUm = 90
Num = 78
teja _garikapathi = 90
a = {'name':'teja',
     'AC_num': '342576878'}
b = {'name':'garikapati',
     'AC_num'='64836826897'}
c = {'name':'ampolu',
    'AC_num' ='34267375679'}
SBI_teja_details ={'name' = 'teja',
      'AC_num'='3422725267'}
ICIC_garikapati_details ={'name' = 'garikapati',
      'AC_num'='23235776662'}

>Assiging varibles:
num = 90
print(num)

num_3, num_2 = 56,65
print(num_3)
print(num_2)

>Swaping of varibles:
a , b = 45, 67
print('a=',a)
print('b=',b)
a, b = b, a
print('a=',a)
prnt('b=',b)

Data types and TypeConverstion
1.Numeric
>Float and integer is called as numeric data types
Float
>A number which containes decimal values, we call it as a float datatype
eg
price = 56.9

integer(int)
>A normal number without any decimal values
eg
num = 89
num_2 = 6

2.String
>String is a squance of char that are enclosed in '', "", """"""
>String is immutable
eg
any_ = 'Python is a language
all- = 'Ab,.&[)-+'

3.List
>List is a collection of different datatypes & it is represented by [] that are separated by ,.
>Inside the list we call it as items & it is a mutable
eg
any_ = [1,'python',[5,6]]
print(type(any_))

4.Tuple
>Tuple is collection of different datatypes that are enclose in () &t those are separated by ,.
>Tuple is immutable
eg
nums = (1,89.67,'python',[3,4],(8,9))

5.Dictionary
>Dictionary is a collection of key:value pairs , keys and values are separated by :.
>key and value pair is call it as a item & this item are separated by ,. & it is represent using {}
>In keys place we use immutable datatypes
>In vaues place we can use any datatypes
eg
data_ = {1:2,
        'name':'Teja',
        (2,3):'tuples}
print(data_)

6.Set
>Set is a collection of unique elements and set can't allow any duplicated vales inside it...
>It is represnted by {} and the elements are seprated by ,.
eg
an = {1,2,3}
print(an)

Typeconversion
>float --> int,str
eg-->int
price = 45.78
print(int(price))

-->str
price = 45.78
con = str(price)
print(type(con))

>int-->float,string
eg
num = 78
print(float(num))

-->str
num = 78
con_ =str(num)
print(type(con))

>string-->int,float
eg
do = '10'
print(int(do))

eg
do = '13.3'
print(float(do))

>List-->tuple(),string
eg
nums = [1,2,3,4]
print(tuple(nums))

eg
tuple-->list
eg-->list()
all_ = (3,4,5)
print(list(all))

set--> tuples, list
eg--> tuple()
all_ = {4,5,6}
print(tuple(all_))

>dict--> list
eg--> dict()
details = [('name','teja'),('edu','B.tech')]
print( dict(details))



'''


