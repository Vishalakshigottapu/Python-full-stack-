'''
ran_ = int(input('enter a number:'))
for j in range(1,ran_+1):
    if j % 2 == 0:
        print(f'{j} is even')
    else:
        print(f'{j} is odd')
eg:

ran_ = int(input('enter a number:'))
for j in range(1,ran_+1):
    if j % 2 != 0:
           print(f'{j} is odd')
eg:
ran_ = 13
for j in range(1,ran_+1):
    if j % 2 != 0:
        print(f'{j} is odd')
eg:
nums = [12,23,34,56]
for j in nums:
    if j % 2 == 0:
        print(f'{j} is a even')
    else:
        print(f'{j} is a odd')
eg:
words_ = input("enter a word:")
vowels = 'aeiouAEIOU'
count = 0
for i in words_:
    if i not in vowels:
        count += 1
        print(f'{i} is consonant')
print(count)
eg:
digits_ = [1,2,3,4,5,4,5,7]
empty_ = []
for i in digits_:
    if i not in empty_:
        empty_.append(i)
print(empty_)


# duplictes values
digits_ = (1,3,4,3,1,5)
empty_ = ()
for j in digits_:
    if j  in digits_:
         empty_ += ()
print(f' {j} is duplicate ')


'''
words_ = 'python is a language'
for i in words_:
    if i == ' ':










