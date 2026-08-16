# Write a program that asks the user for an integer and prints the frequency of each digit in that number.

# For example:
# Enter number: 1223334444
# 1 → 1
# 2 → 2
# 3 → 3
# 4 → 4

# Requirements:
# Do not convert the number to a string.
# Handle negative numbers.
# Don't use collections.Counter.

try :
    num=int(input("enter a number : "))
    temp1=num
    string=""
    if num>0:
        while temp1>0:
            a=temp1%10
            if str(a) not in string:
                count=0
                temp=num
                while temp>0:
                    b=temp%10
                    if a==b:
                        count+=1
                    temp//=10
                print(f"{a} --> {count}")
                string += str(a)
            temp1//=10
    else:
        print("please enter a positive integer")
except ValueError:
    print("please enter a valid number")