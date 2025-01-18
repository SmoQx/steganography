from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import base64


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


def string_to_binary(key: str):
    return ''.join(format(ord(char), '08b') for char in key)


def rsa_encrypt(text_to_encrypt: str, password: str) -> str:
    cipher = PKCS1_OAEP.new(RSA.import_key(format_pem_public(password).encode()))
    ciphertext = cipher.encrypt(text_to_encrypt.encode('utf-8'))
    return base64.b64encode(ciphertext).decode('utf-8')


def rsa_decrypt(text_to_encrypt: str, password: str) -> str:
    cipher = PKCS1_OAEP.new(RSA.import_key(format_pem_priv(password).encode()))
    plaintext = cipher.decrypt(base64.b64decode(text_to_encrypt))
    return plaintext.decode('utf-8')


def format_pem_public(pem_key: str) -> str:
    lines = [pem_key[i:i+64] for i in range(0, len(pem_key), 64)]
    return "-----BEGIN PUBLIC KEY-----\n" + "\n".join(lines) + "\n-----END PUBLIC KEY-----"


def format_pem_priv(pem_key: str) -> str:
    lines = [pem_key[i:i+64] for i in range(0, len(pem_key), 64)]
    return "-----BEGIN RSA PRIVATE KEY-----\n" + "\n".join(lines) + "\n-----END RSA PRIVATE KEY-----"


if __name__ == '__main__':
#    pass_with_salt = ""
#    password = "Pa55"
#
#    print(tekst := caesar_cipher(password, gen_shift(password)))
#    print(reversed_caesar(tekst, gen_shift(password)))
#    print(ord('\n'))

    with open('str.pem', 'r') as pub_key_file:
        pub_key = pub_key_file.read()

    encrypted_text = rsa_encrypt("asdfasdf", format_pem_public(pub_key))
    print(encrypted_text)

    with open('str2.pem', 'r') as priv_key_file:
        priv_key = priv_key_file.read()

    decrypted_text = rsa_decrypt(encrypted_text, format_pem_priv(priv_key))
    print(decrypted_text)

