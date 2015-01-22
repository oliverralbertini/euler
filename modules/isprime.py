import math as m
def is_prime(number):
    if number%2 == 0:
        return False
    if number%3 == 0:
        return False
    for i in range(5,int(m.sqrt(number))+1,6):
        if number%i == 0 or number%(i+2) == 0:
            return False
    return True
