"""Problem 1: Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."""

import sys
sys.path.append('../modules')
from summation import multiples_sum

def main():
   sum = multiples_sum(3,999) + multiples_sum(5,999) - multiples_sum(15,999)
   return sum
 
print main()
