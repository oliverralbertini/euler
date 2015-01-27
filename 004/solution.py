import math as m

def palindrome(digits):
    palindromes = []
    if digits < 1:
        return "Please enter an integer greater than or equal to 1."
    if digits == 1:
        return 9
    if digits == 2:
        return None
    half = digits/2
    if digits%2 == 0:
        start1 = start2 = int(m.pow(10,half) - 1)
        halfr = half
    else:
        start1 = int(m.pow(10,half+1) - 1)
        start2 = int(m.pow(10,half) - 1)
        halfr = half + 1
    for i in xrange(start1,1,-1):
        for j in xrange(start2,1,-1):
            test = i*j
            left = str(test)[0:half]
            right = str(test)[halfr:]
            right = right[::-1]
            if left == right:
                palindromes.append(test)
    return max(palindromes)
print palindrome(6)
