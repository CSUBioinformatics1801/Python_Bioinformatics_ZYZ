from math import sqrt
from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

hold=[]
for i in range(200):
    if(is_prime(i)):hold.append(i)
print(hold)