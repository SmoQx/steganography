import numpy as np
import os
import pathlib
from PIL import Image


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


def reversed_caesar(text, shift = 10):
    return caesar_cipher(text, -shift)


def text_to_binary(text):
    binary_data = ''.join(format(ord(char), '08b') for char in text)
    return binary_data


def binary_to_text(binary_data):
    text = ''.join(chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8))
    return text


def hide_text_in_image(image_path, text_to_hide, output_path):
    # Open the image
    img = Image.open(image_path)

    # Convert text to binary
    binary_text = text_to_binary(text_to_hide)
    print(text_to_hide)
    print(binary_text)
    data_index = 0

    # Iterate through each pixel of the image
    for i in range(img.width):
        for j in range(img.height):
            # Get the RGB values of the pixel

            pixel = list(img.getpixel((i, j)))
            
            # Modify the least significant bit of each color channel
            for color_index in range(3):  # 3 color channels (RGB)
                
                if data_index < len(binary_text):
                    pixel[color_index] = (pixel[color_index] & ~1) | int(binary_text[data_index])
                    data_index += 1

            # Update the pixel in the image
            img.putpixel((i, j), tuple(pixel))

    # Save the modified image
    img.save(output_path)


def file_encoder(file_name: pathlib.Path, password: str = "tekst"):
    if password == "tekst":
        with open(file_name) as file_to_encode:
            file = file_to_encode.read()
        np_loaded = np.loadtxt(file_name)
    return pathlib.Path("dane13.txt")


if __name__ == "__main__":
    image_path = "downloads/Simple_light_bulb_graphic.jpg"
    image_path2 =  "downloads/lovepik-simple-picture_500447536.jpg"
    text_to_hide = "Hello, this is a hidden message!"
    hidden_text = caesar_cipher(text_to_hide, 10)
    output_path = "downloads/with_text.png"

    hide_text_in_image(image_path2, hidden_text, output_path)



