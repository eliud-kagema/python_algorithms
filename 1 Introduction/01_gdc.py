# Find the greatest common denominator of two numbers
# Using Euclid's alogorithm

def gcd(a, b):
    while(b != 0):
        t = a
        a = b
        b = t % b

    return a

# testing the function
print(gcd(100, 96)) # should be 12
print(gcd(20, 8)) # should be 4