# def sum_mul(n,m):
#     if(not (isinstance(n,int) and isinstance(m,int) and n>0 and m>0 )):
#         return 'INVALID'
#     res=0
#     inc=n
#     while(inc<m):
#         res+=inc
#         inc+=n
#     return res

def sum_mul(n, m):
    if m>0 and n>0:
        return sum(range(n, m, n))
    else:
        return 'INVALID'

print(sum_mul(5,5))
