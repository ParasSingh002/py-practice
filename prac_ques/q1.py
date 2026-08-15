# Write a program that takes a string from the user and prints:
# the number of characters
# the first 3 characters
# the last 3 characters
# the string reversed
# the string with all spaces removed

line = input("enter a line of text: ")
length=len(line)
print(length)
print(line[0:3])
print(line[length-1:length-4:-1])
print(line[length-1::-1])
print(line.join(" "))