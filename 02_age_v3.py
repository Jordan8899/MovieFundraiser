def number_input(question):
    while True:
        try:
            response = int(input(question))

            if response <= 12 or response >= 130:

                if response <= 12:
                    print("You're too young to be doing this by yourself")

                elif response >= 130:
                    print("Please enter your real age")

            elif 12 <= response <= 130:
                return response

        except ValueError:
            print("Please only input numbers\n")


name = number_input("What's your age? ")
