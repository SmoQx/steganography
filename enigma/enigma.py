import string

class Rotor:
    def __init__(self, wiring, turnover):
        self.alphabet = string.ascii_uppercase
        self.wiring = list(wiring)
        self.turnover = turnover
        self.position = 0
        self.original_position = 0

    def rotate(self, backward=False):
        # Rotate in the backward direction during decryption
        rotation_direction = -1 if backward else 1
        self.position = (self.position + rotation_direction) % 26

    def check_turnover(self):
        return self.position == self.alphabet.index(self.turnover)

    def encrypt_forward(self, letter):
        letter_index = (self.alphabet.index(letter) + self.position) % 26
        encrypted_letter = self.wiring[letter_index]
        return encrypted_letter

    def encrypt_backward(self, letter):
        letter_index = (self.wiring.index(letter) - self.position) % 26
        encrypted_letter = self.alphabet[letter_index]
        return encrypted_letter

class Reflector:
    def __init__(self, wiring):
        self.wiring = list(wiring)

    def reflect(self, letter):
        letter_index = string.ascii_uppercase.index(letter)
        reflected_letter = self.wiring[letter_index]
        return reflected_letter

class EnigmaMachine:
    def __init__(self, rotor_settings, reflector_settings):
        self.rotors = [Rotor(setting[0], setting[1]) for setting in rotor_settings]
        self.reflector = Reflector(reflector_settings)

    def rotate_rotors(self, backward=False):
        for i, rotor in enumerate(self.rotors):
            rotor.rotate(backward=backward)
            # Check turnover for each rotor and rotate the next rotor if needed
            if i < len(self.rotors) - 1 and rotor.check_turnover():
                self.rotors[i + 1].rotate(backward=backward)

    def encrypt_letter(self, letter):
        # Forward pass through rotors
        for rotor in self.rotors:
            letter = rotor.encrypt_forward(letter)

        # Reflector
        letter = self.reflector.reflect(letter)

        # Backward pass through rotors
        for rotor in reversed(self.rotors):
            letter = rotor.encrypt_backward(letter)

        # Rotate rotors (backward during decryption)
        self.rotate_rotors()

        return letter

    def decrypt_letter(self, letter):
        # Backward pass through rotors
        for rotor in reversed(self.rotors):
            letter = rotor.encrypt_forward(letter)

        # Reflector
        letter = self.reflector.reflect(letter)

        # Forward pass through rotors
        for rotor in self.rotors:
            letter = rotor.encrypt_backward(letter)

        # Rotate rotors (forward during decryption)
        self.rotate_rotors(backward=True)

        return letter

    def encrypt_message(self, message):
        encrypted_message = ''
        for char in message:
            if char.upper() in string.ascii_uppercase:
                encrypted_char = self.encrypt_letter(char.upper())
                # Preserve the case of the original character
                encrypted_message += encrypted_char.upper() if char.isupper() else encrypted_char.lower()
            else:
                encrypted_message += char
        return encrypted_message

    def decrypt_message(self, message):
        decrypted_message = ''
        for char in message:
            if char.upper() in string.ascii_uppercase:
                decrypted_char = self.decrypt_letter(char.upper())
                # Preserve the case of the original character
                decrypted_message += decrypted_char.upper() if char.isupper() else decrypted_char.lower()
            else:
                decrypted_message += char
        return decrypted_message

# Example usage
rotor_settings = [('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q'),
                  ('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E'),
                  ('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V')]
reflector_settings = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'

enigma = EnigmaMachine(rotor_settings, reflector_settings)

message = "HELLO"
encrypted_message = enigma.encrypt_message(message)
print("Original Message:", message)
print("Encrypted Message:", encrypted_message)

decrypted_message = enigma.decrypt_message(encrypted_message)
print("Decrypted Message:", decrypted_message)
