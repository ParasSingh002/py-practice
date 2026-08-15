# Write a program that takes a sentence from the user and:
# removes leading/trailing spaces
# converts it to lowercase
# counts how many words it contains
# checks whether it starts with "python"
# replaces every occurrence of "python" with "AI"
# prints the resulting sentence

sentence=input("enter a sentence : ")
sentence=sentence.lstrip()
print(sentence.lstrip())

sentence=sentence.lower()
print(sentence)

word=sentence.split()
print(len(word))

print(sentence.startswith("python"))

sentence=sentence.replace("python","AI")
print(sentence)