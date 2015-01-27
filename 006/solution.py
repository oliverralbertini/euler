"""Problem 6: Sum square difference
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

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
        
