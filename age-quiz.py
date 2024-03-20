# Ask the user for their age and handle non-numeric input
while True:
    user_input = input("Enter your age: ")
    if user_input.isdigit():  # Check if the input is a numeric value
        user_age = int(user_input)
        break
    else:
        print("Please enter a valid age (numeric value).")

# Create the responses based on the user's age
if user_age >= 40:
    print("You're over the hill.")
    if user_age > 100:
        print("Sorry, you are dead.")
elif user_age >= 65:
    print("Enjoy your retirement!")
elif user_age < 13:
    print("You qualify for a kiddie discount.")
elif user_age == 21:
    print("Congratulations on your 21st!")
else:
    print("Age is just a number.")
