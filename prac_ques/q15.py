# Write a program that asks the user for a number and determines whether it is a perfect number.
# A perfect number is equal to the sum of its positive divisors excluding itself.

# Example:
# 6 → Perfect

# because:
# 1 + 2 + 3 = 6

# Also test:
# 28 → Perfect
# 12 → Not Perfect

try:
    num=int(input("enter a number : "))
    
except ValueError:
    print("enter a valid number!!")