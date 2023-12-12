import string

class EnigmaMachine:
    def __init__(self, rotor_settings):
        self.alphabet = string.ascii_uppercase
        self.rotor = list(rotor_settings)

    def encrypt_letter(self, letter):
        letter_index = self.alphabet.index(letter)
        encrypted_letter = self.rotor[letter_index]
        print(letter_index, encrypted_letter)
        return encrypted_letter
    
    def encrypt_message(self, message):
        encrypted_message = ''
        for char in message:
            if char.upper() in self.alphabet:
                encrypted_char = self.encrypt_letter(char.upper())
                # Preserve the case of the original character
                encrypted_char = encrypted_char.upper() if encrypted_char.isupper() else encrypted_char.lower()
                encrypted_message += encrypted_char
            else:
                encrypted_message += char
        return encrypted_message

# Example usage
rotor_settings = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
enigma = EnigmaMachine(rotor_settings)

message = "HELoooo"
encrypted_message = enigma.encrypt_message(message)
print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
