import sys
import math as m
sys.path.append('../modules')
from isprime import is_prime
from prime_factorization import prime_factorization

"""find out the largest prime factor of big_int"""
big_int = 600851475143
#big_int = 13195

def main():
    """in case big_int is prime"""
    if is_prime(big_int) == True:
        return big_int  
    return prime_factorization(big_int)
primes = main()
print primes[-1]
