'''
list
Collecetion of different datatypes that are separated by , and it is represented by []

indexing
positive indexing --> 0
negative indexing --> -1

so = [1,2,3,4,'Python']
print(so[4][-1])

so = [1,2,3,4,'Python']
print(so[-1][-3])

all_=[12,[1,'python',[1,4],(78,[6,7])],['Java',78]]
print(all_[1][3])

len
The function is used to find the number of items present inside list (gives the count of the items
Syntax
data_ = ['Python',[1,2,(90,'Details',[67,0]),(78,'Student')]]
print(len(data_))

slicing
if 2:6 means except 2 it will gives the values 3,4,5,6
eg
data_ = [1,2,3,4,5,6,7]
print(data_[2:6])

concatinate --> side by side
eg
a = [1,2]
b = [3,4]
print(a+b)

append() --> append method will add new items into list at last index position it also
accepts integers and it gives what is there in append(...)
Syntax --> variable_name.append(item)
eg
go = [1,2]
print(go)
go.append(3)
print(go)
go.append(4)
print(go)

eg
a = [1,2]
a.append([3,4])
print(a)

extend()
-> extend() will add the items into a list at last postion but it will give each value as one index inside the list
syntax:
> variable_name.extend(items)
eg:
go = [1,2]
go.extend('python')
print(go)

pop()
->pop() is used to remove item from the list and it will delete based on the index position
syntax:
> variable_name.pop(index_position)
eg:
m = [1,2,3,4, 'python']
m.pop(3)
print(m)

remove()
-> remove() will delete the items based on the value given in it.
syntax:
> variable_name.remove(value)
eg:
m = [3,4,5,'python']
m.remove(4)
print(m)
