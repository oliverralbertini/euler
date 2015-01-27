import sys
import math as m
sys.path.append('../modules')
from isprime import is_prime

def alls_product(terms,trial):
    for i in xrange(0,terms):
        if trial%(i+1) != 0:
            return False
    return True

def smallest_product(terms):
    if terms < 3:
        return "Please use an integer greater than 2."
    primes = []
    product = 1
    for i in xrange(0,terms):
        if is_prime(i+1) == True:
            primes.append(i+1)  
    for i in xrange(0,len(primes)):
        product *= primes[i]
    trial = product
    while True:
        if alls_product(terms,trial) == True:
            return trial
        else:
            trial += product

print smallest_product(20)
