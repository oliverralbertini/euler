import math as m

def prime_factorization(x):
    primes=[]
    i = 2
    while x%i == 0:
        x /= 2
        primes.append(2)
    for i in xrange(3,int(m.sqrt(x))+1,2):
        while x%i == 0:
            x /= i
            primes.append(i)
    return primes

