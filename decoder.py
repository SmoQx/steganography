from PIL import Image
from creat_password import gen_shift


def extract_text_from_image(image_path):
    img = Image.open(image_path)
    binary_data = ""

    for i in range(img.width):
        for j in range(img.height):
            pixel = list(img.getpixel((i, j)))

            for color_index in range(3):
                # Extract the least significant bit from each color channel
                binary_data += str(pixel[color_index] & 1)

    # Convert binary data to text
    extracted_text = binary_to_text(binary_data)

    return extracted_text


def binary_to_text(binary_data):
    text = ''.join(chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8))
    return text


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


if __name__ == "__main__":
    image_path = "./downloads/output.png"

    extracted_text = extract_text_from_image(image_path)
    tekst_to_display = caesar_cipher(extracted_text, -(gen_shift("tekst")))

    print("Extracted Text:", tekst_to_display[:50])
