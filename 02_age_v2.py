# While not loop to only allow numbers giving user infinite attempts
i = False
while not i:
    age = int(input("What is your age? "))
    if 12 <= age < 130:
        i = True
    # Elif statement so that if they input too low of a number or too high it corrects them
    elif age <= 12 or age > 130:
        if age <= 12:
            print("You're too young to be doing this by yourself")
        else:
            print("Please enter your real age")

    # Error message that gets displayed if the user inputted anything other than a number
    elif age != int:
        print("You may only input numbers\n")
