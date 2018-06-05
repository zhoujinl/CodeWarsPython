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

'''
find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
'''
def find_uniq_string(arr):
    # do the magic
    newmap = {}
    for x in arr :
         newmap["".join(set(sorted(str(x).lower().strip())))] = x
    arr = map(lambda x : "".join(set(sorted(str(x).lower().strip()))),arr)
    arr = sorted(arr)
    return newmap[arr[-1] if arr[0] == arr[1] else arr[0]]

#s = find_uniq_string([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ])
#s1 = find_uniq_string([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ])
#s3 = find_uniq_string([  '    ', '  ', ' ', 'a', ' ', '' ])
s2 = find_uniq_string(['', '', '', 'a', '', '' ])

print(s2)
print(s2)
