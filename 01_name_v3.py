def check_input(question):
    while True:
        try:
            response = str(input(question))

            if response.isalpha():
                return response
            else:
                print("Please input only letters\n")

        except ValueError:
            print("Error\n")


name = check_input("What's your name? ")
