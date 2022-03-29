# Name question for user to answer with their name if name != letters error
name = input("What is your name? ")
if name.isalpha():
    print(name)
else:
    print("Your name must be only letters")
