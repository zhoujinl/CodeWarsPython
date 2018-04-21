# -*- coding:utf-8 -*-
import re

'''
solve("3(ab)") = "ababab" -- "ab" repeats 3 times
solve("2(a3(b))" = "abbbabbb" -- "a3(b)" == "abbb" repeats twice.

字符串反转的2种方法：
s1 = s[::-1]
s1 = reversed(s)
'''

def solve(st):
    #python 贪婪匹配和非贪婪匹配，第一个分组是非贪婪，故用.*? ；第二个分组是贪婪，故用 .*
    mult = lambda x, y: int(x) * y if x.isdigit() else x + y
    m = re.match('(.*?)\((.*)\)',st,re.L)
    strBefore = ""
    if m :
        x = m.group(1)
        y = m.group(2)
        print(x, y)
        istr = re.match('([a-zA-Z]*)(\d*)',x,re.L)  # y="2(ax3(b))"  针对这种情况
        if istr :
            strBefore = istr.group(1)
            x = istr.group(2)  #只用数字列替换
        if str(y).find("(") > 0 :
            y = solve(y)
    return (strBefore + mult(x,y))

def solve1(s):
    s1 = s[::-1]  #字符串反转
    print(s1)
    s2 = ''
    for i in s1:
        if i.isalpha():
            s2 += i
        elif i.isdigit():
            s2 = s2*int(i)
    return s2[::-1]

def solve3(s):
    return solve(re.sub(r'(\d*)\(([a-zA-Z]*)\)', lambda m: m.group(2) * (1 if m.group(1) == "" else int(m.group(1))),
                        s)) if re.search(r'(\d*)\(([a-zA-Z]*)\)', s) != None else s


x="2(ab)"
y="3(b(2(c)))"  #bccbccbcc
z="k(a3(b(a2(c))))"  # kabaccbaccbacc
print(reversed(z))    #reversed(z) 字符串反转
print(solve(z))
