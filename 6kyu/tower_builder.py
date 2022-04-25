# def tower_builder(n_floors):
#     l=[]
#     l_len=n_floors*2-1
#     for i in range(1,n_floors+1):
#        y=str('*'*(i*2-1))
#        line=str(' '*(int((l_len-len(y))/2)))
#        l.append(line+y+line)
#     return l

def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]

print(tower_builder(3))

