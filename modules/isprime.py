import math as m
"""use to determine if a number is prime, but must be larger than 3."""
def is_prime(number):
    #if number == 2 or number == 3:
        #return True
    if number%2 == 0 or number%3 == 0:
        return False
    for i in range(5,int(m.sqrt(number))+1,6):
        if number%i == 0 or number%(i+2) == 0:
            return False
    return True

