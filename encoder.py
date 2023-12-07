import numpy as np
import os
import pathlib


def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Encrypt uppercase letters
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            # Encrypt lowercase letters
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result


def encrypt_file(file_path, shift):
    try:
        with open(file_path, 'r') as file:
            plaintext = file.read()

        encrypted_text = caesar_cipher(plaintext, shift)

        with open(file_path, 'w') as file:
            file.write(encrypted_text)

        print("Encryption successful.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def file_encoder(file_name: pathlib.Path, password: str = "tekst"):
    if password == "tekst":
        with open(file_name) as file_to_encode:
            file = file_to_encode.read()
        np_loaded = np.loadtxt(file_name)
    return pathlib.Path("dane13.txt")


if __name__ == '__main__':
    file_encoder(pathlib.Path("dane13.txt"))

