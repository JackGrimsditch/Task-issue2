# ask the user for their age and save as user_age
user_age = int(input("Enter your age: "))

#create the responses that differ based on the users input, using the if, elif and else functions
if user_age >= 40:
    print("you're over the hill")
    if user_age > 100:
        print("sorry, you are dead")
elif user_age >= 65:
    print("enjoy your retirement")
elif user_age < 13:
    print("you qualify for a kiddie discount")
elif user_age == 21:
    print("congratulations on your 21st!")
else:
    print("age is just a number")