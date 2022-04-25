def find_it(seq):
    for a in seq:
        if seq.count(a)%2:
            return a

# def find_it(seq):
#     return [x for x in seq if seq.count(x) % 2][0]


print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))