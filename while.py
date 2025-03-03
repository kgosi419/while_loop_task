""" The objective of the program is to add the numbers the user enters
until they enter -1, using the while loop then calculate the average"""

# Initialise variables to track and count the users input
total = 0
count_input = 0

user_input = float(input("Enter any number: "))

while user_input != -1:
    total += user_input
    count_input += 1

    user_input = float(input("Enter any number: "))
  
    if user_input == -1:
        average = (total / count_input)
        print("Average:",(round( average, 2)))
        break
