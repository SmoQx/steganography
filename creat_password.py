import numpy as np
import random


def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Encrypt uppercase letters
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
                print(result)
            # Encrypt lowercase letters
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
                print(result)
        else:
            result += char
    return result


def encrypt_text(file_path, shift):
    try:
        with open(file_path, 'r') as file:
            plaintext = file.read()

        encrypted_text = caesar_cipher(plaintext, shift)

        with open(file_path, 'w') as file:
            file.write(encrypted_text)

        print("Encryption successful.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


    def create_salt():
        pass


if __name__ == '__main__':
    pass_with_salt = ""
    password = "pass"
    if len(password) < 33 and len(password) > 1:
        for _ in range(len(password), 33):
            rand = random.randint(65, 123)
            rand_character = chr(rand)
            password += rand_character
            print(password)

    print(caesar_cipher(pass_with_salt, 10))

