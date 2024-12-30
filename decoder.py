from PIL import Image
from creat_password import gen_shift, caesar_cipher, rsa_decrypt


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
    text = ''
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if byte == '00000000':
           break  # Stop decoding when encountering '00000000'
        text += chr(int(byte, 2))
    return text


def decode_file(file_path, password):
    extracted_text = extract_text_from_image(file_path)
    tekst_to_display = caesar_cipher(extracted_text, -(gen_shift(password)))

    return tekst_to_display


def decode_file2(file_path: str, password: str) -> str:
    extracted_text = extract_text_from_image(file_path)
    tekst_to_display = rsa_decrypt(extracted_text, password)

    return tekst_to_display


if __name__ == "__main__":
    image_path = "downloads/output.png"
    file_path = "./downloads/pobrane.jpeg"
    extracted_text = extract_text_from_image(image_path)
    tekst_to_display = caesar_cipher(extracted_text, -(gen_shift('pass')))
    print("Extracted Text:", tekst_to_display)

