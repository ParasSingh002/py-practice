# Write a program that asks the user for a password and checks whether it:

# contains at least 8 characters
# contains at least one uppercase letter
# contains at least one lowercase letter
# contains at least one digit
# contains at least one special character
# contains no spaces

# Print "Strong password" only if all conditions are satisfied; otherwise print which requirements are missing.

while True:
    upcase=0
    lcase=0
    digit=0
    special=0
    space=0
    pwd=input("Please enter the password : ")

    if len(pwd)>=8:
        for i in pwd:
            if i.isspace():
                space+=1
        if space == 0:
            for i in pwd:
                if i.isupper():
                    upcase+=1
                elif i.islower():
                    lcase+=1
                elif i.isdigit():
                    digit+=1
                #or " elif not i.isalnum(): "
                else:
                    special+=1

            if upcase>=1 and lcase>=1 and digit>=1 and special>=1:
                print("STRONG PASSWORD !!")
                break
            else:
                print("\nPlease make sure that atleast one of these are included :")
                if upcase==0:
                    print("> uppercase")
                if lcase==0:
                    print("> lowercase")
                if digit==0:
                    print("> digit")
                if special==0:
                    print("> special")

        else:
            print("please exclude the spaces")
    else:
        print("Short password")