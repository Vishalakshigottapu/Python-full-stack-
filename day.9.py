'''
Set
-> set is a unordered collection of elements
-> NO duplicate allowed in the set
-> set is represented by {}
eg:
nums = {1,2,3,}
print(nums)

Operations:
Union():
->The union() will combine two sets into a single set
syntax:
> set_1.union(set_2) or set_1 | set_2
eg:
data_={1,2,3,4}
nums = {5,6}
print(data_.union(nums))
print(data_ | nums)

intersection():
-> this will gives us the common elements from both sets
> syntax:
set_1.intersection(set_2) or set_1 & set2
eg:
data_ = {1,2,3,4}
nums = {2,3,6}
print(data_.intersection(nums))
print(data_ & nums)

difference():
-> it will dispaly the difference element from set_1, but not the set_2 elements
syntax:
>set_1.difference(set_2) or set_1
data_ = {1,2,3,4}
nums = {2,3}
print(data_.difference(nums))

symmetric():
->difference elements from the both
syntax:
>set_1,symmetric_difference(set_2) or set_1 ^ set_2
eg:
data_ = {1,2,3,4}
nums = {3,4}
print(data_.symmetric_differnece(nums))

METHODS:
add():
-> add() method will add only one element at a time
syntax:
set.add(element)
eg:
data_ = {1,2,4}
print(data_)
data_.add(7)
print(data_)

update():
-> we can add more than one elements by using update method
syntax:
> set.update([elements]) or set_1.update(set_2)
eg:
data_ = {1,2,3}
nums = {4,56}
print(data_)
data_.update([9,11])
print(data_)

remove():
-> remove() it will del the element from the set, if the element is not present in the set,it will raise error
syntax:
>data_remove(element)
eg:
data_ = {1,2,3,4}
data_.remove(3)
print(data_)
data_.remove(5)
print(data_)

discard():
-> the method is used to del the elements from the set, but never raise any error even the element not insied set
>syntax:
set.discard(element)
eg:
data_ = {1,2,3}
data_.discard(3)
print(data_)
data_.discard(7)
print(data_)

clear():
->the method is used to del all elements from the set and it will return empty set
syntax:
> set.clear()
eg:
data_ = {1,2,3}
data_.clear()
print(data_)














