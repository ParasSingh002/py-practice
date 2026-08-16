# Write a program that asks the user for a sentence and creates a new sentence where:
# the first and last character are swapped
# all spaces are removed
# all letters are converted to lowercase
# the program prints the original and modified sentence

sentence=input("enter a sentence : ")
new= sentence[-1] + sentence[1:-1] + sentence[0]

new=new.replace(" ","")

new=new.lower()

print("Original sentence is : ",sentence)
print("Modified sentence is : ",new)
