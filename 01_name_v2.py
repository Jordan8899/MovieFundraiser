i = False
while not i:
    name = input("What is your name? ")
    if name.isalpha():
        i = True
    else:
        print("Your name may only have letters\n")
