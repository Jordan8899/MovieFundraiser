# Age variable only allowing numbers as the input otherwise it errors
age = input("What's your age? ")
if age.isnumeric() and age >= 12 < 130:
    print(age)
else:
    print("\nPlease only input numbers")