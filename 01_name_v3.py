# String value checker function, same as v2 except this code can be recalled
def string_input(question):
    while True:
        try:
            response = str(input(question))

            if response.isalpha():
                return response
            else:
                print("Please input only letters\n")

        except ValueError:
            print("Error\n")


# Name variable calling the function
name = string_input("What's your name? ")
