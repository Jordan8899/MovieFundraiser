# Age variable only allowing numbers as the input otherwise it errors
age = int(input("What's your age? "))
if age >= 12 and age < 130:
    print(age)

elif age < 12 or age > 130:
    print("Please enter a valid age")

else:
    print("\nPlease only input numbers")
