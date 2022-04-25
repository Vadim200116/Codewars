# https://www.codewars.com/kata/525c65e51bf619685c000059/train/python
import math


def cakes(recipe, available):
    res=10000
    for k in recipe:
        if k not in available:
            return 0
        a=math.floor(available[k]/recipe[k])
        if a<res:
            res=a
    return res
        

# def cakes(recipe, available):
#     return min(available.get(k, 0)/recipe[k] for k in recipe)



print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))