from PIL import Image


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

if __name__ == "__main__":
    image_path = "path/to/output/image_with_hidden_text.png"
    
    extracted_text = extract_text_from_image(image_path)

    print("Extracted Text:", extracted_text)


if __name__ == '__main__':
    pass
