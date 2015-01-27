import math as m
def is_prime(number):
    if number == 1 or number == 2 or number == 3:
        return True
    if number%2 == 0:
        return False
    if number%3 == 0:
        return False
    for i in range(5,int(m.sqrt(number))+1,6):
        if number%i == 0 or number%(i+2) == 0:
            return False
    return True
