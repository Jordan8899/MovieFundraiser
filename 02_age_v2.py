i = False
while not i:
    age = int(input("What is your age? "))
    if 12 <= age < 130:
        i = True

    elif age <= 12 or age > 130:
        if age <= 12:
            print("You're too young to be doing this by yourself")
        else:
            print("Please enter your real age")

    elif age != int:
        print("You may only input numbers\n")
