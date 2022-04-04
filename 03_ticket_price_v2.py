# Number checker function that can be called infinite times
def number_input(question):
    while True:
        try:
            response = int(input(question))

            # If statement checking viable age
            if response < 12 or response >= 130:

                if response < 12:
                    print("You're too young to be doing this by yourself")

                elif response >= 130:
                    print("Please enter your real age")

            elif 11 < response <= 130:
                return response

        # Error message if user inputs incorrect characters
        except ValueError:
            print("Please only input numbers\n")


# Age variable using number_input function
age = number_input("What's your age? ")

# Ticket Price
if age in range(12, 15):
    ticket_price = 7.5

elif age in range(16, 64):
    ticket_price = 10.5

elif age in range(65, 130):
    ticket_price = 6.5

print(ticket_price)
