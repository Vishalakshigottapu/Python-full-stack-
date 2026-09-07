'''
MATH:
import math
print(math.pi)
print(math.ceil(4.3))
print(math.floor(5.6))
print(math.sqrt(25))
print(math.sin(2))
print(math.pow(2,3))
print(math.cos(5))

RANDOM:
import random
print(random.randint(100000,999999))
print(random.randrange(1,100))
color = ['red','pink','blue']
print(random.choice(color))
random.shuffle(color)
print(color)

PLATFORM:
import platform
print(platform.python_version())
print(platform.system())
print(platform.platform())
print(platform.processor())

COLLECTIONS:
import collections
data_ = ['banana','apple','banana','orange','orange']
print(collections.Counter(data_))
all_ = collections.Counter(data_)
print(all_.most_common())

from collections import defaultdict
data_ = defaultdict(list)
data_['python'].append('teja')
data_['python'].append('raju')
data_['java'].append('sony')
print(data_)

DATE /TIME
from datetime import datetime
today = datetime.today()
print(today.day)
print(today.month)
print(today.year)
print(today.minute)
print(today.hour)

from datetime import datetime
now = datetime.now()
print(now.strftime('%d-%m-%y'))
print(now.strftime('%H:%M:%S'))
print(now.strftime('%a'))

import random
attempts = 3
num = random.randrange(1,100)
print(num)
while attempts > 0:
    game = int(input('enter a number between 1 and 100:'))
    if game == num:
        print('your guess is correct')
        break
    else:
        attempts -=1



import random
attempts = 3
num = random.randrange(1,100)
print(num)
while attempts > 0:
    game = int(input('enter a number between 1 and 100:'))
    if game == num:
        print('your guess is correct')
        break
    else:
        attempts =- 1
if attempts == 3:
    print('price money is 500')
elif attempts == 2:
    print('price money is 200')
elif attempts == 1:
    print('price money is 100')
else:
    print('better luck next time')


ITERTOOLS:
import itertools
a = itertools.count(45)
print(next(a))
print(next(a))
b = itertools.repeat('python',6)
for j in b:
    print(j)
c = itertools.cycle(['python','java','c'])
for j in c:
    print(j)
'''
import itertools
n = itertools.chain([1,2,3],[5,6,7])
print(list(n))

import math
print(math.pow(3,4))

