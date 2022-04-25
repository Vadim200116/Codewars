# https://www.codewars.com/kata/51e056fe544cf36c410000fb/python

import re

def top_3_words(text):
    l=text.lower().split(" ")
    res={}
    for w in l:
        w=re.sub(r'[^\w\s]','', w)
        if not w.isalpha():
            continue
        if w in res.keys():
            res[w]+=1
        else:
            res[w]=1
    sorted_res=sorted(res.items(),key=lambda x:-x[1])
    return [*dict(sorted_res)][:3]

print(top_3_words("  //wont won't won't will wi w wi f f "))
