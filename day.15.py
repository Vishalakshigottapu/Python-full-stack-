'''
#Palindrome
words = input("enter a word:")
empty_str = ''
for i in words:
    empty_str = i + empty_str
if empty_str == words:
    print(f"{words} is a palindrome")
else:
    print(f"{words} is not a palindrome")

#Amstrong
num = int(input("enter a number"))
length_ = len(str(num))
amstrong_ = 0
for i in str(num):
    amstrong_ = amstrong_ + int(i)**length_
    print(amstrong_)
if amstrong_ == num:
    print(f'{num} is Amstrong number')
else:
    print(f'{num} is not Amstrong number')

#perfect number
num = int(input("enter a number"))
any_ = 0
for i in range(1,num):
    if num %i == 0:
        any_+=i
if any_ == num:
    print(f'{num} is a perfect number')
else:
    print(f'{num} is not a perfect number')

#fibanocci series
num = 0
num_2 = 1
print(num,num_2,end=' ')
for i in range(1,10):
    num_3 = num + num_2
    num = num_2
    num_2 = num_3
    print(num_3,end=' ')
'''





    
