import sys
import math as m
sys.path.append('../modules')
from isprime import is_prime

"""find out the largest prime factor of big_int"""
big_int = 600851475143
#big_int = 13195

def main():
    if is_prime(big_int) == True:
        return big_int  
    for i in xrange(2,int(big_int/2)):
        if big_int%i == 0:
            if is_prime(big_int/i) == True: 
                return big_int/i
    return "none"
print main()
