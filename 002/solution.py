"""find the sum of the even members of the Fibonacci sequence not exceeding 4,000,000."""
max = 4000000
term = 2
prev_term = 1
even_sum = 0
new_term = term
while term < max:
    even_sum += term
    """every 3rd number is even in the Fibonacci sequence"""
    for x in range(0,3):
        new_term += prev_term 
        prev_term = term
        term = new_term
print even_sum
