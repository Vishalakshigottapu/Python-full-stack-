'''
Dictionary():
->Dict is a collection of key : value pair
->Key must be unique and it should bu immutable datatype(int,str,tuple)
-> it was represented in {}
eg:
details = {1: 2,
           'name':'vishala',
           (1,2):[1,2]}
print(details)

Accessing():
->dict can access by calling key, we will get value from that key
>snytax:
dict['key']
get() method is also used to get the value from that key
>syntax:
dict.get(key)
eg:
data_ = {'name': 'vishala',
        'balance': 7000,
        'aadhar': 23074550403,
        'PANC':'DGNVUGIUFNKSI'}
print(data_)
print(data_['aadhar'])
print(data_.get('PANC'))
UPDATE():
-> method is used to update a key, incase if the key is not present inside dict then it add that key:value
>syntax:
dict.update({key:value})
#there is a another way update a key
>synatx dict[key] = value
eg:
eg:
data_ = {'name': 'vishala',
        'balance': 7000,
        'aadhar': 23074550403,
        'PANC':'DGNVUGIUFNKSI'}
print(data_)
data_.update({'name':'swapna'})
data_.update({'ATMPIN':2343})
print(data_)

VALUES():
->values() method is used get all the value from the dict
>syntax:
dict.values()
KEYS():
->keys()method is used get all the from the dict
>syntax:
dict.keys()
ITEMS():
-> the method will get the key : value separated from the dict
>syntxa:
dict.items()
CLEAR():
->clear method is used to del all the from dict
>syntax:
dict.clear()
data_ = {'name': 'vishala',
        'balance': 7000,
        'aadhar': 23074550403,
        'PANC':'DGNVUGIUFNKSI'}
print(data_.values())
print(data_.keys())
print(data_.items())
del data_['aadhar']
print(data_.clear())



 ####STATEMENTS####
1.if statement:
>if is a condition become true, then it will execute inside block of code
>In case it become false ,then it will never entry inside
eg:
age = 19
if age>=18:
    print('Eligible to vote')
print(age)
eg:
a = 90
b = 78
if a>b:
    print(a)

if-else:
-> else for if statment is a fall-back statement, incase if condition is false then block will execute
eg:
age = 19
if age>=18:
    print(f'your {age} Eligible to vote')
else:
    print(f'your {age} you have to wait {18-age}')

eg:
a = 90
b = 7870
if a>b:
    print(a)
else:
    print(b)

