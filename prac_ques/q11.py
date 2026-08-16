# Write a program that asks the user to enter a positive integer and repeatedly performs this operation:
# If the number is even, divide it by 2.
# If the number is odd, multiply it by 3 and add 1.
# Continue until the number becomes 1.

# Print every value produced.

# For example, starting with 6:
# 6
# 3
# 10
# 5
# 16
# 8
# 4
# 2
# 1
# Also print how many steps were required

steps=0
try:
    num=int(input("please enter a positive integer : "))
    if num>0:
        print(num)
        while True:
            if num%2==0:
                num//=2
            else:
                num=num*3 +1

            steps+=1
            print(num)

            if num==1:
                    break
    else:
        print("please enter a positive integer")

except ValueError:
        print("please enter a valid number!!")

print("Total steps taken are : ",steps)