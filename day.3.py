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


