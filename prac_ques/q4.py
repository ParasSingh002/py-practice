# Write a program that asks the user for their name and marks in 3 subjects. Store the subject marks appropriately,
# calculate the total and average, and print:
# the student's name
# total marks
# average
# "Pass" if every subject is at least 40
# "Fail" otherwise

name=input("enter your name : ")
while True:
    if name.isalnum !=True:
        maths=int(input("enter your marks in maths out of 100 : "))
        try:
            if maths<=100 and maths>=0:
                sci=int(input("enter your marks in science out of 100 : "))

                if sci<=100 and sci>=0:
                    eco=int(input("enter your marks in eco out of 100 : "))

                    if eco<=100 and eco>=0:
                        print(name)
                        print("your total marks out of 300 is : ",maths+sci+eco)
                        print("your average marks is : ",(maths+sci+eco)/3)

                        if maths>=40 and sci>=40 and eco>=40:
                            print("PASS")
                        else:
                            print("FAIL")
                        break
                    
                    else:
                        print("please enter a valid number")
                else:
                    print("please enter a valid number")
            else:
                print("please enter a valid number")

        except ValueError:
            print("please enter numerical value only")

    else:
        print("please enter a valid name!")
