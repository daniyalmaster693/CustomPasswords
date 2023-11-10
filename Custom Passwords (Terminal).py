import secrets
import string


def generate_password (length, use_letters = True, use_numbers = True, use_symbols = False):
    characters = ""

    if use_letters:
        characters += string.ascii_letters


    if use_numbers:
        characters += string.digits


    if use_symbols:
        characters += string.punctuation


    if not characters:
        raise ValueError ("You must select a character, number or symbol to create your password")
    
    
    password = ''.join(secrets.choice (characters) for _ in range (length))
    return password

    
while True:
    try:
        password_length = int (input ("Enter a number between 1 and 12 as the length of your password: "))
        if 1 <= password_length <= 12:
            break
        
        else:
            print ("Please enter a valid number between 1 and 12")
   
    except ValueError:
        print ("Please enter a number between 1 and 12")


use_letters = input ("Would you like your password to include letters. Enter yes or no:").lower() == "yes"
use_numbers = input ("Would you like your password to include numbers. Enter yes or no:").lower() == "yes"
use_symbols = input ("Would you like your password to include symbols. Enter yes or no:").lower() == "yes"


password = generate_password (password_length, use_letters, use_numbers, use_symbols)
print (f"Here is your password: {password}")