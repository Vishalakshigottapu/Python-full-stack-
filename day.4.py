'''
concatinaton
-> The + will behave two ways for numaric if works normally and for other datatypes like string, list, tuple it concatination.

>Operators
->The operstors are used to perform operations in variables and the values.
1.Arthematic Operator
+, -, *, /, //, %
eg
num = 78
num_2 = 9
print(num + num_2)
eg for -sub
a = 3
b = 1
print(a - b)
eg *mul
v = 8
n = 4
print(v*n)
eg /div
v = 8
n = 4
print(v / n)
print(v // n)
print(v % n)

2.Assignment Operator
=, +=, -=, *=, %=, /=
+= -> it is a increment operator
eg
a = 0
print(a)
a += 1
print(a)
-= ->decrement operator
b  = 67
b -= 5
print(b)

*= ->
c = 7
c *= 2
c = c + 1
print(c)
%=
v = 34
v %= 3
print(v)
/=
s = 32
s /= 2
print(s)

3.Comparison Operator
==, >=, <=, >, <, !=
eg
num = 9
num_2 = 5
print(num == num_2)# 9 == 5
print(num != num_2)#9 != 5
print(num > num_2)# 9 > 5
print(num < num_2) 9 < 5
>=
num = 10
num_2 = 9
print(num >= num_2)
print(num <= num_2)

4.logical operator
AND
OR
NOT
eg AND
num = 9
num_2 = 13
print(num >= num_2 and num <= 10)# 9 >= 13 and 9 <= 10
print(num <= num_2 and num >= 10)# 9 >= 1 and 9 >= 10
OR
num = 9
num_2 = 13
print(num >= num_2 or num < 10)
NOT
num = 9
num_2 = 13
print(not(num >= num_2 or num < 10))

5.Identity Operator
is, isnot
eg
num = [1,2]
num_2 = [1,2]
print(num is num_2)
isnot
a = [1,2]
b = [1,2]
print(id(a))
print(id(b))
print(a is not b)

6.Membership Operator
in, notin
num = [1,2,56,78]
print(8 in num)
print(23 not in num)
7.Bitwise Operator
5 --> 0101
3 --> 0011
1 --> 0001
print(5 & 3)

| --> Bitwise or 
5 --> 0101
3 --> 0011
7 --> 0111
print(5 / 3)

^ --> Bitwise XOR
5 --> 0101
3 --> 0011
6 --> 0110
print(5 ^ 3)

>> --> Right shift
5 --> 0101
1 --> 0001
0001
print(5 >> 2)

<< --> left shift
5 --> 0101
10 --> 1010
print(5 << 1)

