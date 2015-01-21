def multiples_sum (k, n):
    """terms is the number of termis in the sum"""
    """k is the spacing"""
    terms = n/k
    sum = terms*(2*k+k*(terms-1))/2
    return sum
