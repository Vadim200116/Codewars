# https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python


# import heapq

# def queue_time(customers, n):
#     heap = [0] * n
#     for time in customers:
#         heapq.heapreplace(heap, heap[0] + time)
#     return max(heap)
    


# def queue_time(customers, n):
#     if(len(customers)<1):
#         return 0
#     if(len(customers)<=n):
#         return max(customers)
#     q_iter=customers[0:n]
#     while(len(customers)>n):
#         q_iter.sort()
#         q_iter[0]+=customers.pop(n)
#     return max(q_iter)

def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)

print(queue_time([1,2,3,4,5], 1))