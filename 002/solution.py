"""Problem 2: Even Fibonacci numbers
    Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""

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
