import random
import string


def generate_password():
    length = int(input("Enter password length: "))

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print(f"Generated Password: {password}")


print("PASSWORD GENERATOR")

generate_password()