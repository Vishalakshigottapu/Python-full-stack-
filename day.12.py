'''
loops:
for statement:
->A for loop is used to over a squence or iterable datatypes
*after for num is defined this varible at run to store values from itrabledatatypes
eg:
nums = [12,3,5,78]
for num in nums:
    print(num)
else in for
-> unlike if-else, else block in for statement is executed after completed of all iteration
eg:
nums = [12,3,5,78]
for num in nums:
    print(num)
else:
    print('for ended')
Break:
-> The break used to stop iteration based on the condition given
eg:
nums = [1,2,3,4,5]
for num in nums:
    print(num)
    if num == 3:
        break
eg:
val_ = [1,2,3,4,5]
for j in val_:
    if j % 2 == 0:
       print(f'{j} is even')
    else:
       print(f'{j} is odd')
       
Continue:
->The continue is keyword used to skip the current iteration based on the condtion
eg:
nums = [1,2,3,4,5,8,9]
for num in nums:
    if num == 5:
       continue
    print(num)
pass:
-> A pass is called as space holder, that is used after statement like (if,for,else)not to raise error 
eg:
for j in range(1,11):
    if j == 15:
       print(j)
    else:
        pass

assert:
-> assert is a keyword used to check the condition, incase the condition is false, it will raise the error(assertion error)
eg:
age = 19
assert age >= 18
print('your eligible to vote')

While:
num = 1
while num <= 5:
     print(num)
     num += 1

























