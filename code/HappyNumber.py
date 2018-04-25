# -*- coding:utf-8 -*-

'''
For example, the number 7 is a "happy" number:

72 = 49 --> 42 + 92 = 97 --> 92 + 72 = 130 --> 12 + 32 + 02 = 10 --> 12 + 02 = 1

Once the sequence reaches the number 1, it will stay there forever since 12 = 1

On the other hand, the number 6 is not a happy number as the sequence that is generated is the following:
6, 36, 45, 41, 17, 50, 25, 29, 85, 89, 145, 42, 20, 4, 16, 37, 52, 29
'''
def is_happy(n):
    # Good Luck!
    values =[]
    #value = reduce(lambda x,y: x+y,map(lambda i : int(i)*int(i), str(n)))
    f_value = lambda n : sum(map(lambda i : int(i)*int(i), str(n)))
    while(True):
        n = f_value(n)
        if(n == 1): return True;
        if(values.__contains__(n)):return False;
        values.append(n);


print(is_happy(7))

## other method
def is_happy1(n):
    while n > 4:
        n = sum(int(d)**2 for d in str(n))
    return n == 1

def is_happy2(n):
    seen = set()
    while n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1

def is_happy3(n):
    while n > 100:
        n = sum(int(d) ** 2 for d in str(n))
    return True if n in [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109, 129,
                         130, 133, 139, 167, 176, 188, 190, 192, 193, 203, 208, 219, 226, 230, 236, 239, 262, 263, 280,
                         291, 293, 301, 302, 310, 313, 319, 320, 326, 329, 331, 338, 356, 362, 365, 367, 368, 376, 379,
                         383, 386, 391, 392, 397, 404, 409, 440, 446, 464, 469, 478, 487, 490, 496] else False




