# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/

# import re

# def increment_string(strng):
#     n = re.findall(r'\d+', strng)
#     if not n:
#         return strng+"1" 

#     num=int(n[0])+1

#     return strng[:-len(n[0])]+"{:0{x}d}".format(num,x=len(n[0]))

from collections import namedtuple

def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))

print(increment_string("foo"))

