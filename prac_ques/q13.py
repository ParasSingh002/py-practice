# Write a program that repeatedly asks the user to enter integers until 0 is entered.

# At the end, print:

# Total numbers entered
# How many were even
# How many were odd
# Average of all numbers
# The second-largest number

# Rules:
# Ignore 0 in all calculations.
# Invalid input must not terminate the program.
# Don't use Python's built-in sort(), max(), or min().

# This one is considerably harder because you'll need to maintain several pieces of information while the loop is running.

entries=0
n_odd=0
n_even=0
sum=0
max1=None
max2=None
i=0
while True:
    try:
        num=int(input("enter a number : "))

        if num==0:
            break
        else:
            if num%2==0:
                n_even+=1
            else:
                n_odd+=1
            entries+=1
        
        sum+=num
        if max1==None and max2==None:
            max1=num
            max2=num
            i=1
        else:
            if num>max1 and i==1:
                max2=max1
                max1=num
            elif i==1:
                max2=num
                i=2
            elif i==2 and num>max1:
                max2=max1
                max1=num
            elif i==2 and num>max2:
                max2=num

    except ValueError:
        print("please enter a valid number!!")

print("Total numbers entered are : ",entries)
print("Total even numbers entered are : ",n_even)
print("Total odd numbers entered are : ",n_odd)
print("Average of all numbers entered is : ",sum/entries)
print("The second largest number entered is ",max2)