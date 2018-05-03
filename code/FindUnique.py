# -*- coding:utf-8 -*-
'''
There is an array with some numbers. All numbers are equal except for one. Try to find it!

findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
It’s guaranteed that array contains more than 3 numbers.
The tests contain some very huge arrays, so think about performance.

'''


def find_uniq_number(arr):
    arr.sort()
    return arr[-1] if arr[0] == arr[1] else arr[0]

def find_uniq_number1(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

i = find_uniq_number([ 1, 1, 1, 2, 1, 1 ])
print(i)