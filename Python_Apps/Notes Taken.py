
# <editor-fold desc="Section01">
# .format()
age = 5
print("I am " + str(age) + " years old.")
print("I am {} years old.".format(age)) # {} is a placeholder

age = 5
month = 6
print("I am {} years adnd {} months old.".format(age, month))

# name the placeholder
"I am {age_} years old, are you {age_} years old too?".format(age_=age)
"This {} is {age} years old.".format("person", age=25)

# input() # ask user for a value
user_age = input("Enter your age: ")
seconds = int(user_age) * 365 * 24 * 60 * 60
print("You have lived for {} seconds.".format(seconds))

# create a function to prevent the user from typing in codes
def age_in_seconds():
    user_age = input("Enter your age: ")
    seconds = int(user_age) * 365 * 24 * 60 * 60
    print("You have lived for {} seconds.".format(seconds))

# age in second program
def age_program():
    seconds_or_years = input("Give me seconds (s) or years (y)?")
    if seconds_or_years == "s":
        user_value = input("Enter the number of seconds you've lived for: ")
        print("You've lived for {} years".format(int(user_value) / 60 / 60 / 24 / 365))
    elif seconds_or_years == "y":
        user_value = input("Enter the number of seconds you've lived for: ")
        print("You've lived for {} seconds".format(int(user_value) * 60 * 60 * 24 * 365))

# guess a number program
def guess_a_number_program():
    import random
    n = random.randint(1, 9)
    guess = int(input("Enter an integer from 1 to 9. You have 3 chances! "))
    i = 0
    while i < 3:
        if guess < n:
            i += 1
            guess = int(input("Too Small! You can guess {} more time! Guess Again!".format(3-i)))
        elif guess > n:
            i += 1
            guess = int(input("Too Large! You can guess {} more time! Guess Again!".format(3-i)))
        else:
            i += 1
            print("Smart!")
            break
    print("Play Again!")
# </editor-fold>

# install homebrew and use homebrew to install mongodb
# https://brew.sh/ # homebrew website
# https://treehouse.github.io/installation-guides/mac/mongo-mac.html # instructions
