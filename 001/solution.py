import sys
sys.path.append('../modules')
from summation import multiples_sum

def main():
   sum = multiples_sum(3,999) + multiples_sum(5,999) - multiples_sum(15,999)
   return sum
 
print main()
