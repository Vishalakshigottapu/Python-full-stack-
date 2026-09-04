'''
LIST COMPREHENSION:
-> list comprehension is the shortest from of syntax to create a list
syntax:
[expression loop condition]
[expression condition else loop]
eg:
old_ = (1,2,3,4,8)
new_ = [i for i in old_]
print(new_)
eg:
old_ = (1,2,3,4,8)
new_ = [i for i in old_ if i%2==0 ]
print(new_)

nested comprehension
-> using list comprehension generating list inside list
eg:
any_ = [[i*j for i in range(1,4)] for j in range(1,8)]
print(any_)
eg:
a = [[1,2,3],[4,5,6],[9,7,8]]
any = [num for j in a for num in j]
print(any)

generator:
-> the generator is a special function which genarate one value at a time
eg:

def all_():
    for j in range(1,100):
        yield j
j = all_()
print(next(j))
      
