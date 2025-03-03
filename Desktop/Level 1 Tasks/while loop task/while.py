""" The objective of the program is to add the numbers the user enters
until they enter -1, using the while loop then calculate the average"""

# Initialise variables to track and count the users input
total = 0
count_input = 0
sentinel = -1

user_input = input("Enter any number (or -1 to exit): ")

while True:
    try:
        user_input = float(user_input)

        if user_input == sentinel:
            if count_input == 0:
                print("No numbers were entered.")
            else:
                average = total / count_input
                print("Average:", round(average, 2))
            break

        total += user_input
        count_input += 1

    except ValueError:
        print("Invalid input. Please enter a valid number.")

    user_input = input("Enter any number (or -1 to exit): ")
