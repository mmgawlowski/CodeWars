'''
Given a string that includes alphanumeric characters ('3a4B2d') return the expansion of that string: The numeric values represent the occurrence of each letter preceding that numeric value. There should be no numeric characters in the final string. Empty strings should return an empty string.

The first occurrence of a numeric value should be the number of times each character behind it is repeated, until the next numeric value appears.

string_expansion('3D2a5d2f') == 'DDDaadddddff'
string_expansion('3abc') == 'aaabbbccc'       # correct
string_expansion('3abc') != 'aaabc'           # wrong
string_expansion('3abc') != 'abcabcabc'       # wrong
If there are two consecutive numeric characters the first one is ignored.

string_expansion('3d332f2a') == 'dddffaa'
If there are two consecutive alphabetic characters then the first character has no effect on the one after it.

string_expansion('abcde') == 'abcde'
Your code should be able to work for both lower and capital case letters.

string_expansion('') == ''
'''

import re
def string_expansion(s):
    list = re.findall('[0-9][a-z]+', s, re.I)
    bl = re.findall('^[a-z]+', s, re.I)
    str_bl = str(bl).strip("[]'' ")
    if not bl:
        bl = ''
    if not list: return ''.join(x for x in s if x.isalpha())
    else: 
        for x in list:
            for i in range (len(x)):
                if x[i].isalpha():
                    value = int(x[0])*x[i]
                    str_bl += value
    return str_bl
