# -*- coding:utf-8 -*-
'''
Your task is to write a function that does just what the title suggests (so, fair warning, be aware that you are not getting out of it just throwing a lame bas sorting method there)
with an array/list/vector of integers and the expected number n of smallest elements to return.
first_n_smallest([1,2,3,4,5],3) == [1,2,3]
first_n_smallest([5,4,3,2,1],3) == [3,2,1]
first_n_smallest([1,2,3,4,1],3) == [1,2,1]
first_n_smallest([1,2,3,-4,0],3) == [1,-4,0]
first_n_smallest([1,2,3,4,5],0) == []

取数组中最小的N个数，并且按原来的顺序输出
'''

def first_n_smallest(arr, n):
    if n == arr.__len__() : return arr
    sa = sorted(arr)
    mid = sa[ n-1 if n!=0 else 0 ]
    lesscount =0
    for v in arr:
        if v<mid : lesscount+=1
    newa = []
    for v in arr :
        if newa.__len__() < n :
            if v < mid  : newa.append(v)
            if v == mid and n-lesscount>0:
                newa.append(v)
                lesscount+=1
    return newa

#print(first_n_smallest([2,1,2,1,5],3))
print(first_n_smallest([1,2,3,4,5],3))
#print(first_n_smallest([7, 7, -8, 4, 2, -1, 5, -1, 8, 10, 0, 6, 10, 3, 3, -5, -10, 0, 7, 2, 1, 8, 7, 8],3))
#print(first_n_smallest([2, -1, 2, 2, 3, 1, 8, 1],5))
print(first_n_smallest([5, 2, -7, -5, -4, -1, -4, -10, -3, -4, -2, 3, 2, 2, -4, 4, 4, 2, -9, 10, -8, -4, -10, -6, 2, 7, 3, 9, -7, -2, -7, -6, -1, 8, 4, -3, 1, 10, -7],24))


def first_n_smallest1(arr, n):
    return [e[0] for e in sorted(sorted([[arr[i],i] for i in range(len(arr))])[:n],key=lambda x:x[1])]

def first_n_smallest2(arr, n):
    return [x[1] for x in sorted(sorted(enumerate(arr), key=lambda x: x[1])[:n])]

print(first_n_smallest2([5, 2, -7, -5, -4, -1, -4, -10, -3, -4, -2, 3, 2, 2, -4, 4, 4, 2, -9, 10, -8, -4, -10, -6, 2, 7, 3, 9, -7, -2, -7, -6, -1, 8, 4, -3, 1, 10, -7],24))
