# Write a program that asks the user to enter a number and determines whether it is a prime number.

# Requirements:

# 1 should not be considered prime.
# Handle negative numbers and 0.
# The program should not crash if the user enters something that isn't an integer.
# Don't convert the number to a string to solve it

try:
    num=int(input("enter a number : "))
    if 0<num!=1:
        count=0
        for i in range(2,num+1):
            if(num%i)==0:
                count+=1
        if count==1:
            print("Prime")
        else:
            print("Composite")
    else:
        print("Negative integers,0 & 1 are neither prime nor composite")
except ValueError:
    print("please enter a valid number!!")
