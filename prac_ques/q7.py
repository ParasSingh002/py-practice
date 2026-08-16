# Write a program that asks the user for a sentence and determines whether it is a palindrome, ignoring:

# spaces
# capitalization
# punctuation

sentence=input("Please enter a sentence : ")
temp=""

for i in sentence:
    if i.isalnum():
        temp += i.lower()

reverse=temp[::-1]
print(reverse)

if temp==reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")