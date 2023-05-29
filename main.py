import random
import string

def generate_password (min_length, number = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

    if number == True:
        characters += digits
    if special_characters == True:
        characters += special  
        
          

    

generate_password(10) 