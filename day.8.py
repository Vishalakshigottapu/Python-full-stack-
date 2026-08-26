'''
Tuple
-> Tuple is a collection of different datatype that separated by, and represented by ()
-> it is immutable
-> we can pass a tuple value and that can be asgin to the variables,but it should match same number variables and values inside the tuple
eg:indexing
t = (1, 'python', [3,4], (7,9))
print(t[2][1])

index()
-> if item is not present in the tuple, it will raise value error
t = (1, 'python', [3,4], (7,9))
print(t.index('python'))

len()
t = (1, 'python', [3,4], (7,9))
print(len(t))
eg:
name, age, batch = ('vishala', 21, 6)
print(name)
print(age)

max()
-> used to find the max value from the tuple
eg:
so = (4,56,78)
print(max(so))

min()
-> used to find the min value from the tuple
eg:
so = (2,45,667,0)
print(min(so))

count()
->used to count an item present in the tuple
eg:
so = (2,2,34,4,2,5)
print(so.count(2))

concardtion
so = (42,34,56)
do = (34,34)
print( so + do)

