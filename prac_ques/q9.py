# Write a program that asks the user for a number and prints the following pattern:

# For input:
# 5

# output:
# 54321
# 5432
# 543
# 54
# 5

try :
    num=int(input("enter a number : "))
    n=num
    i=num
    while i!=1:
        solve=n*10 + i-1
        n=solve
        i=i-1

    # n = 0
    # for i in range(num, 0, -1):
    #     n = n * 10 + i

    while n>0:
        print(n)
        n=n//10

except ValueError:
    print("please enter a valid number")