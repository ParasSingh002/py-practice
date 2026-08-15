# Write a program that repeatedly asks the user for a number until they enter 0. For every number entered
# determine whether it is positive or negative. At the end, print how many positive and negative numbers were entered.

positive_num=0
negative_num=0
while True:
    try:
        num=int(input("enter a number : "))
        if num==0:
            break
        elif num>0:
            positive_num+=1
        elif num<0:
            negative_num+=1
    except ValueError:
        print("please enter a valid number")
        
print(f"total positive numbers are {positive_num}")
print(f"total negative numbers are {negative_num}")