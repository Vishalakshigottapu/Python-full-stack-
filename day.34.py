'''
Variable length arguments(*args), Keyword variable length arguments(**kwargs)
Variable length argumnets -- We can pass any number of arguments, but the data will be stored in a tuple, but we use symbolically *args as representation

def new(*a):
    """Usage of variable length arguments"""
    print(a)
    print(type(a))
#new()#it returns empty tuple as we didn't pass any args
#new(1,2,3)
#new(12,3)
#new("codegnan","vishala","swapna",34)
details =[1234,'data','webinar','hackathon']
new(details)#in this case list is stored inside a tuple as a single obj.
new(*details)#in this case we can extract the values from the above list as a tuple.
a,b,c = 1,3,4
a,*b,c=1,"vishala","swpana","frnds",34
print(a)
print(c)
print(b)


#*is mainly used to unpack the values from a collection
a = ['codegnan','python','data',45,6.7]
print(*a)
for i in a:
    print(i,end=' ')
#in above case both for loop and line 32 result is same.   


#Task:Find the sum of arguments in a function
def add(*a):
    """sumof aguments usage *args"""
    print(a)
    print(type(a))
    #we need to have output varible
    result = 0
    for i in a:
        if type(i) == int or type(i)== float:
                result = result + i              
    return result
    #print(result)          
#print(add())
#print(add(1,3,4))
print(add(12,3,4,'codegnan','vishala',2.4))

#Keyword variable length arguments-->We can pass any number of keyword arguments, we will use the representation as **kwargs, data is stored in dictionary.

def admission(**Kwargs):
    """usage of keyword variable length arguments"""
    print(Kwargs)
    print(type(Kwargs))
#admission()#empty dict
#admission(name='vishala',mobile=7396260191,email_id='swpanalovesme@codegnan.com')

details ={'idnos':[234,345,342],
          'names':['swapna','meena','vishali'],
          'batches':['DA','PFS','JFS']}
admission(**details)
'''
#usage of both *args and **kwargs into a function
def simple(*a,**b):
    """usage of *args and **Kwargs"""
    print(a)
    print(b)
    result = 0
    for i in a:
        if type(i) == int or type(i)== float:
                result = result + i              
    print(result)
    for key,value in b.items():
        print(f'key is {key}')
        print(f'value is {value}')
simple()
simple(1,2,3,'poll',23,name='codegnan',place='vizag')
#simple(23,4,batch='PFS6',data='python',3.5)#positional arguments always follow keyword argumnets

    



















