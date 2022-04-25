# def find_uniq(arr):

#     s=sum(arr[i] for i in range(0,int(len(arr))))
#     if arr[0]==arr[1]:
#         if isinstance(arr[0],float):
#             return s-(arr[0]*(len(arr)-1))
#         return s-(arr[0]*(len(arr)-1))
#     elif arr[0]==arr[2]:
#         return arr[1]
#     else:
#         return arr[0]


def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
    
print(find_uniq([ 0, 0, 0.55, 0, 0 ]) )