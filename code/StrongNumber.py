# -*- coding:utf-8 -*-

import math

# A number is called strong number if sum of the factorial of its digits is equal to number itself !!
# 1! + 4! + 5! = 1 + 24 + 120 = 145
# strong_num (1)  return "STRONG!!!!"
# strong_num (2 )  return "STRONG!!!!"
# strong_num (123) return "Not Strong !!"
# strong_num (150)  return "Not Strong !!"

import math
def strong_num(number):
    sum=0
    for s in str(number):    
        sum = sum + math.factorial(int(s))
    if sum == number return "STRONG!!!!" else  return "Not Strong !!"

#优雅的写法        
def strong_num1(number):
    return "STRONG!!!!" if sum(math.factorial(int(i)) for i in str(number)) == number else "Not Strong !!"
