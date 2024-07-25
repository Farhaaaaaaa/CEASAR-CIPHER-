import pyfiglet

def display_fancy_text(text):
    # Create a fancy text using pyfiglet with a specific font
    fancy_text = pyfiglet.figlet_format(text)
    print(fancy_text)

# Replace "Fancy Software" with your software name
display_fancy_text("CEASAR  CIPHER")

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(text, shift):
    encrypted_text = ""
    for char in text.upper():
        if char in alphabets:
            location_of_character = alphabets.find(char)
            new_location = (location_of_character + shift) % 26
            encrypted_text += alphabets[new_location]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text.upper():
        if char in alphabets:
            location_of_character = alphabets.find(char)
            new_location = (location_of_character - shift) % 26
            decrypted_text += alphabets[new_location]
        else:
            decrypted_text += char
    return decrypted_text

# ANSI escape code for red text
red_text = "\033[91m"
reset_text = "\033[0m"

# Prompt the user for the operation
operation = input(red_text+ "Press E to encrypt a plain text or D to decrypt a cipher text:"+ reset_text).upper()

# Ask the user for the input string and the shift value
string_input = input("Enter the string: ")
shift_input = int(input("Enter the value to shift by: "))

if operation == 'E':
    result = encrypt(string_input, shift_input)
    print("Encrypted text:", result)
elif operation == 'D':
    result = decrypt(string_input, shift_input)
    print("Decrypted text:", result)
else:
    print("Invalid operation selected. Please enter E for encryption or D for decryption.")
