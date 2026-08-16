# Write a program that asks the user to enter a number and determines whether it is an Armstrong number.

# Examples:
# 153 → Armstrong
# 370 → Armstrong
# 123 → Not Armstrong

# For a 3-digit number, an Armstrong number is one where the sum of the cubes of its digits equals the original number.
# Your program should work for any positive integer, not only 3-digit numbers.

try:
    num=int(input("please enter a number : "))
    temp=num
    solve=0
    while temp>0:
        d=temp%10
        solve+=d**3
        temp//=10
    if num==solve:
        print("armstrong number")
    else:
        print("not an armstrong number")
except ValueError:
    print("please enter a valid number!!")