

# import math
# def is_square(n):
#     return n > -1 and math.sqrt(n) % 1 == 0



def is_square(n):
    if(n<0):
        return False
    for a in range(n+1):
        if a*a==n:
            return True
        if a*a>n:
            return False
    # return False


print(is_square(25))
print(is_square(2))