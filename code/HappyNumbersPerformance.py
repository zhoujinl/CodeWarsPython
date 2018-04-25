# coding=utf-8
'''
performant_numbers(10) ==> [1, 7, 10]
performant_numbers(50) ==> [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49]
performant_numbers(100) ==> [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100]
Test suite:
5000 tests with number n being up to 300000
As the reference solution takes around 4.6 seconds to get the result, you are left with only 6.9 more
you are not allowed to hardcode the sequence: you'll have to compute it (max length of the code: 1700 characters)
HappyNumer 性能升级版，有时间限制等
'''
import HappyNumber
import time
### Execution Timed Out
def performant_numbers(n):
    # good luck
    return list(filter(lambda i : HappyNumber.is_happy3(i),range(1,n+1)))

# is_happy 15-20-25s
# is_happy1 8-10s
# is_happy1 10-15-20s
print(time.time())
#print(performant_numbers(1000))
#performant_numbers(299999)
print(time.time())

############################################################################
############################################################################

b = [False]
a = []
a2 = [None]

def f(n):
    def is_happy(n):
        s = {n}
        while n != 1:
            nn = 0
            while n > 0: nn += (n%10)**2; n//=10
            n = nn
            if n < len(b): return b[n]
            if n in s: return False
            s.add(n)
        return True
    for k in range(1, n+1):
        b.append(is_happy(k))
        if b[k]: a.append(k)
        a2.append(len(a))
f(300000)

def performant_numbers1(n):
    return a[:a2[n]]

print(time.time())
#print(performant_numbers(1000))
performant_numbers1(123456)
print(time.time())

############################################################################
############################################################################

from bisect import bisect
LIMIT = 1 + 300000
happySieve = [None] * LIMIT
happySieve[1] = 1


def happyOnes(n):
    seen = set()
    while 1:
        if happySieve[n] is not None: return happySieve[n], seen
        if n in seen or n == 1:  return n == 1, seen
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))


for n in range(1, LIMIT):
    isH, seen = happyOnes(n)
    for x in seen: happySieve[x] = isH

HAPPY = [i for i in range(1, LIMIT) if happySieve[i]]


def performant_numbers2(n): return HAPPY[:bisect(HAPPY, n)]

print(time.time())
#print(performant_numbers(1000))
performant_numbers2(123456)
print(time.time())

############################################################################
############################################################################

# generate happy numbers up to LIMIT
LIMIT = 300000
HAPPY, SAD = set(), set()

for n in range(1, LIMIT + 1):
    seen = set()
    while True:
        seen.add(n)
        n = sum(d * d for d in map(int, str(n)))

        if n == 1 or n in HAPPY:
            HAPPY |= seen
            break
        elif n in seen or n in SAD:
            SAD |= seen
            break

HAPPY = sorted(HAPPY)

from bisect import bisect


def performant_numbers(n):
    return HAPPY[:bisect(HAPPY, n)]