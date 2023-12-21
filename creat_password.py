

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


def reversed_caesar(text, shift=10):
    return caesar_cipher(text, -shift)


def gen_shift(password):
    value = 0
    for _ in password:
        value += ord(_)
    return value


if __name__ == '__main__':
    pass_with_salt = ""
    password = "Pa55"

    print(tekst := caesar_cipher(password, gen_shift(password)))
    print(reversed_caesar(tekst, gen_shift(password)))
    print(ord('\n'))

