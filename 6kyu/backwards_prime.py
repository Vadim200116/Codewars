# def is_prime(num):
#     if num==2 or num==3: return True
#     if num%2==0 or num<2: return False
#     for i in range(3, int(num**0.5)+1, 2):
#         if num%i==0:
#             return False
#     return True

# def rev(num):
#     return int(''.join(reversed(str(num))))

# def backwards_prime(start, stop):
#     lis=[]
#     if start<10:
#         start=12
#     while start<stop+1:
#         if is_prime(start) and is_prime(rev(start)) and rev(start)!=start:
#             lis.append(start)
#         start+=1
#     return sorted(lis)


def backwards_prime(start, stop):
    primes = []
    for n in range(start, stop+1):
        if n not in primes and is_prime(n) and is_prime(reverse(n)) and n != reverse(n):
            primes.append(n)
            if start <= reverse(n) <= stop:
                primes.append(reverse(n))
    return sorted(primes)

def is_prime(n):
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

def reverse(n):
    return int(''.join(str(n)[::-1]))


print(backwards_prime(1,97))

