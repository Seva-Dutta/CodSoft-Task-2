import random
import string
def generate_password (length):

    custom_symbols = '@#$%&'    # Here, I have used some custom symbols that will be generated in the password. To use any punctuation symbol we can use 'string.punctuation'.
    letters = string.ascii_letters
    digits = string.digits

    all_chars = letters + digits + custom_symbols

    password = ''.join(random.choices(all_chars, k=length))
    return password

while True:
    try:
        print("\nPress '0' to exit")
        length = int(input("Enter the password length ; "))
        if (length == 0):
            print("\nExiting progam")
            break
        elif length<4:
            print("\nPassword length should be more.")
            continue
        else:
            print("\nGenerated password : ",generate_password(length))
            
    except ValueError:
        print("\nInvalid input.")

    
