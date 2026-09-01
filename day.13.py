'''
limit_ = 10
for i in range(1,limit_+1):
    for j in range(1,i+1):
        print(j)
eg:
limit_ = 10
for i in range(2,limit_+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(f'{i} is prime')
eg:
star_ = int(input("enter a number:"))
for i in range(1,star_+1):
    for j in range(1,i+1):
        print('*',end=" ")
    print()
'''
star_ = int(input("enter a number:"))
count = 0
for i in range(1,star_+1):
    for j in range(1,i+1):
        count += 1
        print(count,end=" ")
    print()
