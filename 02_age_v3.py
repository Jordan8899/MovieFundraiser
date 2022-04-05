# Number checker function that can be called infinite times
def age_check(question):
    while True:
        try:
            response = int(input(question))

            # If statement checking viable age
            if response not in range(12, 130):

                if response <= 12:
                    print("You're too young to be doing this by yourself")

                elif response >= 130:
                    print("Please enter your real age")

            elif response in range(12, 130):
                return response

        # Error message if user inputs incorrect characters
        except ValueError:
            print("Error, please only input numbers\n")


# Age variable using number_input function
age = age_check("What's your age? ")
