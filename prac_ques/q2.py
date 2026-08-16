# Write a program that repeatedly asks the user to enter numbers. Stop when they enter 0. At the end, print:

# number of positive values
# number of negative values
# sum of all positive values
# sum of all negative values
# largest number entered
# smallest number entered

# Invalid input such as "abc" should not crash the program.


positive_num=0
negative_num=0
sum_p=0
sum_n=0
min=None
max=None

def min_max(min,max,num):
    if num>max:
        max=num
    if num<min:
        min=num
    return min,max

while True:
    try:
        num=int(input("enter a number : "))

        if num==0:
            break

        if min == None:
            min=num
            max=num
        else:
            min,max=min_max(min,max,num) 

        if num>0:
            positive_num+=1
            sum_p+=num
            if min == None:
                min=num
        elif num<0:
            negative_num+=1
            sum_n+=num

    except ValueError:
        print("please enter a valid number")

print(f"total positive numbers are : {positive_num}")
print(f"Sum of positive numbers is : {sum_p}")
print(f"total negative numbers are : {negative_num}")
print(f"Sum of negative numbers is : {sum_n}")
print(f"Minimun number is : {min}")
print(f"Maximum number is : {max}")