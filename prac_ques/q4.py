# Write a program that asks the user for their name and marks in 3 subjects. Store the subject marks appropriately,
# calculate the total and average, and print:
# the student's name
# total marks
# average
# "Pass" if every subject is at least 40
# "Fail" otherwise

while True:
    name=input("Please enter your name : ")
    if name.replace(" ","").isalpha():
        break
    print("please enter a valid name!!")

while True:
    try:
        maths=int(input("enter maths marks out of 100 : "))
        sci=int(input("enter science marks out of 100 : "))
        eco=int(input("enter economics marks out of 100 : "))

        if 0<=maths<=100 and 0<=sci<=100 and 0<=eco<=100:
            break
        print("please enter number between 0 to 100 only") 

    except ValueError:
        print("please enter a valid number!!")

total = maths + sci + eco
average = total / 3

print("\nName:", name)
print("Total marks out of 300:", total)
print("Average:", round(average,2))

if maths >= 40 and sci >= 40 and eco >= 40:
    print("PASS")
else:
    print("FAIL")