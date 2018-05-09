# -*- coding:utf-8 -*-

'''
A string is considered to be in title case if each word in the string is either (a) capitalised
 (that is, only the first letter of the word is in upper case) or (b) considered to be an exception and put entirely into lower
case unless it is the first word, which is always capitalised.

将参数A 里面的单词全部改成首字母大写其余小写，而参数B里面的则是要排除转换的单词（第一个单词一定要转换的）。
title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
title_case('the quick brown fox') # should return: 'The Quick Brown Fox'
'''

def title_case(title, minor_words=""):
    if title == "" :  return ""
    lt = str(title).title().split()
    nt = list()
    nt.append(lt[0])
    for s in lt[1:] : nt.append(str(s).lower() if str(minor_words).lower().split().__contains__(str(s).lower()) else str(s))
    return " ".join(nt)

print(title_case('a clash of KINGS', 'a an the of'))
print(title_case('First a of in','an often into'))
print(title_case(''))

def title_case2(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])

def title_case3(title, minor_words=''):
  return ' '.join(w if w in minor_words.lower().split() and i else w.capitalize() for i, w in enumerate(title.lower().split()))


def title_case4(title, minor_words=''):
    return ' '.join(c if c in minor_words.lower().split() else c.title() for c in title.capitalize().split())


print(title_case2(''))
