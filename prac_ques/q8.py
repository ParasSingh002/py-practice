# Write a program that asks the user for a number and prints the following pattern:

# For input:
# 5

# output:
# 1
# 12
# 123
# 1234
# 12345

try:
    num=int(input("enter a number : "))
    n=1
    i=1
    while i<=num:
        print(n)
        solve=n*10 + i+1
        n=solve
        i+=1
except ValueError:
    print("please enter a valid number : ")