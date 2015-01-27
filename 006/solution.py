import sys
import math as m
sys.path.append('../modules')
from summation import multiples_sum

def sum_square_difference(number):
    terms = []
    square_sum = 0 
    for i in xrange(0,number):
        terms.append(i+1)
    for i in xrange(0,number):
        square_sum += terms[i]*terms[i]
    sum = multiples_sum(1,number)
    return sum*sum - square_sum
            

print sum_square_difference(100)
        
