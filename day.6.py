'''
Strings
Operations:
1.Indexing
->Indexing is usde to get char that you looking to access
1.postive indexing
-> it will starts from 0 index
syntax -> print(variable_name[index_position])
text = 'python'
print(text[2])

2.negative indexing
->it will starts from -1 index
syntax -> print(variable_name[negative_index])
text = 'swapna'
print(text[-3])
eg:
txt = 'python is a programming language'
print(txt[-15])
print(txt[17])

len()
-> len is a built-in function that is used get number of char present in the string
syntax -> len(variable_name)
eg:
text = 'python'
print(len(text))

Slicing
-> this is used to access the particular part from the string
syntax -> variable_name[start:end]
eg:
text = 'python is a programming language'
print(text[12:23])
print (text[12:])
print(text[:23])
print(text[::-1])

Upper()
-> used to convert all small char into cap
eg:
txt = 'python is a programming language'
print(txt.upper())

Lower()
-> used to convert all cap into small
eg:
txt = 'Python is a Programming Language'
print(txt.lower())

index
eg:1
txt = 'Python is a Programming Language'
print(txt.index('r'))
2.sub string
txt = 'Python is a Programming Language'
print(txt.index('r',2,15))

replace()
-> used to replace with old string with new string
syntax:
-> variable _name.replace(old,new)
eg
txt = 'python is a programming language'
print(txt.replace('python', 'java'))

split()
>this method is used to seprate the string based on given substring
syntax:
txt = 'python is a programming language'
print(txt.split(' '))
eg:
txt = 'Python is a Programming Language'
print(txt.split(' '))

Count()
>it is used to count number of occurrences of an substring
syntax:
variable_name.count('substring')
eg:
txt = 'Python is a Programming Language'
print(txt.count('a',1,16))


