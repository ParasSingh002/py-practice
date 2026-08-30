# Write a program that repeatedly accepts integers until the user enters 0. At the end, print:
# Largest number
# Smallest number
# Second largest number
# Second smallest number
# Number of positive values
# Number of negative values
# Average

# Rules:
# 0 is only the termination value and must not be included in the calculations.
# Invalid input must not crash the program.
# Don't use sort(), max(), or min().
# Handle the case where fewer than two numbers were entered.

max1=None
max2=None
min1=None
min2=None
solve=0
n_positive=0
n_negative=0
i=0
try:
    while True:
        num=int(input("enter a number : "))
        if num!=0:
            if max1==None and max2==None and min1==None and min2==None:
                max1=num
                max2=num
                min1=num
                min2=num
                i=1
            if num>max1 and i==1:
                max2=max1
                max1=num
            if num<min1 and i==1:
                min2=min1
                min1=num

            if num>0:
                n_positive+=1
            else:
                n_negative+=1
                n_negative+=1

            solve+=num
        else:
            break

    print(f"Largest numnber is {max1}")
    print(f"Second largest numnber is {max2}")
    print(f"Smallest numnber is {min1}")
    print(f"Second smallest numnber is {min2}")
    print(f"Total positive numnber are {n_positive}")
    print(f"Total negative numnber are {n_negative}")
    print(f"Average of all numnber entered is {round(solve/(n_positive+n_negative),2)}")
except ValueError:
    print("Please enter a valid number!")
