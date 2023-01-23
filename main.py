import random
import string


def password_generator(length, use_uppercase, use_numbers, use_special_characters):
    # create a string of possible characters to use in the password
    possible_characters = string.ascii_letters
    if use_uppercase:
        # add uppercase letters to possible characters
        possible_characters += string.ascii_uppercase
    if use_numbers:
        # add digits to possible characters
        possible_characters += string.digits
    if use_special_characters:
        # add special characters to possible characters
        possible_characters += "!@#$%^&*()_+-=[]{};:,.<>/?\""
    # generate a random password of specified length
    # using a list comprehension and the "random.choice" function
    # to randomly select characters from "possible_characters",
    # and join them together to create a string password of specified length
    password = ''.join(random.choice(possible_characters) for _ in range(length))
    return password


# prompt the user for desired password length
password_length = int(input("Enter the desired length of the password: "))
# prompt the user for whether to use uppercase letters
use_uppercase = input("Do you want to use uppercase letters? (y/n)").lower() == 'y'
# prompt the user for whether to use numbers
use_numbers = input("Do you want to use numbers? (y/n)").lower() == 'y'
# prompt the user for whether to use special characters
use_special_characters = input("Do you want to use special characters? (y/n)").lower() == 'y'

# generate and print the password
password = password_generator(password_length, use_uppercase, use_numbers, use_special_characters)
print(password)
