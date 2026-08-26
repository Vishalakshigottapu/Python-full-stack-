'''
elif:
->elif statement is used to check more possible outcomes or more condition
eg:1
a = 90
b = 780
c = 670
if a>b and c>a:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
eg:    
num = 7
num_2 = 3
user_opt = int(input('enter \n1.add \n2.sub \n.3mul \n4.pow:'))
if user_opt == 1:
    print(num + num_2)
elif user_opt == 2:
    print(num - num_2)
elif user_opt == 3:
    print(num * num_2)
else:
    print(num ** num_2)

nested if:
-> if inside an if statement is called nested if
eg:
app_details = {'pin':1234}
import random
user_pass = int(input("Enter your app password:"))
otp = random.randint(1000,9999)
if user_pass == app_details['pin']:
   print('password is correct')
   print(otp)
   user_otp = int(input("Enter 4 digit OTP:"))
   if user_otp == otp:
       print('welcome to the app')
   else:
       print('incorrect OTP')
else:
    print('password is incorrect')

eg:
1.
a = int(input("enter a number"))
if a % 2 == 0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')

2.
'''
marks_ = int(input("enter your marks:"))
if marks_>=90:
    print('A+')
elif marks_>=80:
    print('A')
elif marks_>70:
    print('B+')
elif marks_>60:
    print('B')
elif marks_>50:
    print('C+')
elif marks_>40:
    print('C')
else:
    print('Fail')
















    
        

    
