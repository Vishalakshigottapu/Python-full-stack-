'''
#Funtions
-> A function is a block of code that can be excuted only when it is called
-> A function start with def keyword and the line called as definition line, where we can define a function name
-> And if we want to execute in the function, need to call with the function name the function name define at def line
syntax:
def fun_name(parameters):
    pass
fun_name(arguments)
Arguments:
postional Arguments:
->The argument should be same at def line and calling, incase if they are not same number will raise an error 
ex:
def add_(a,b):
    print(a+b)
add_(5,6)


num = 0
num_2 = 1
def add_(num,num_2):
    print(num,num_2,end=' ')
    for i in range(1,10):
        num_3 = num + num_2
        num = num_2
        num_2 = num_3
        print(num_3,end=' ')
add_(num,num_2)

Default arugments:
-> The default arguments where the function will only consider the data at calling, even though data present at def line
eg:
def feb_(num,num_2):
    print( num + num_2)
feb_([1,3],[5,6])
eg:
def data_(a=8,b=6):
    print(a+b)
    data_(1,2)

eg:
def prime(num=10,count = 1):
    for j in range(1,num+1):
        if num % j == 0:
            count += 1
            print(count)
    if count == 2:
        print(f'{num} is prime')
    else:
        print(f'{num} is not prime')
prime(num = int(input("enter a number:")),count=0)


#keyword arguments
-> Keyword arguments are sending arguments in a pair(a=2),and the order is not consider
eg:
def data_(age,name,batch,location):
    print(name)
    print(age)
    print(batch)
    print(location)
data_(name='vishala',age=22,location='Vizag',batch=6)

#Variable Length arguments:
->Adding a (* call it as args) before a varible at parameters
->We can pass tuple of arguments and can be access with indexing
eg:
def all_(*name):
    print(name)
all_('vishala','gottapu','swapna','ampolu')

Keyword Length arguments:
->adding a ** (call it as k args) before a varible at parameter
->We can pass varibles length arguments and can be access
eg:
def details(**data_):
    print(data_.keys())
details(name='vishala',age=22,location='Vizag',batch=6)
Return :
->Return keyword used inside the function, once the return is executed,means it will get back to the calling with return values
eg:
def all_(a,b):
    return a-b
print(all_(7,9))





