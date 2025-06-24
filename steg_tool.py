import argparse
from PIL import Image

def encode_image(input_image_path, output_image_path, message):
    # Force RGB mode
    image = Image.open(input_image_path).convert("RGB")
    encoded = image.copy()
    width, height = image.size
    message += chr(0)  # End marker
    binary_message = ''.join([format(ord(c), '08b') for c in message])
    data_index = 0

    for y in range(height):
        for x in range(width):
            if data_index >= len(binary_message):
                break
            r, g, b = encoded.getpixel((x, y))
            r = (r & ~1) | int(binary_message[data_index])  # Set LSB
            data_index += 1
            encoded.putpixel((x, y), (r, g, b))
        if data_index >= len(binary_message):
            break

    try:
        encoded.save(output_image_path)
        print(f"[+] Message encoded and saved to {output_image_path}")
    except Exception as e:
        print(f"[!] Failed to save image: {e}")

def decode_image(input_image_path):
    image = Image.open(input_image_path).convert("RGB")
    width, height = image.size
    binary_data = ""
    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            binary_data += str(r & 1)

    chars = [chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8)]
    message = ''.join(chars)
    end_index = message.find(chr(0))
    if end_index != -1:
        message = message[:end_index]
    print(f"[+] Hidden message: {message}")

def main():
    parser = argparse.ArgumentParser(description="Steganography Tool")
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    encode_parser = subparsers.add_parser('encode', help='Encode a message into an image')
    encode_parser.add_argument('-i', '--input', required=True, help='Input image file (PNG)')
    encode_parser.add_argument('-o', '--output', required=True, help='Output image file')
    encode_parser.add_argument('-m', '--message', required=True, help='Message to encode')

    decode_parser = subparsers.add_parser('decode', help='Decode a message from an image')
    decode_parser.add_argument('-i', '--input', required=True, help='Image file to decode from')

    args = parser.parse_args()

    if args.command == 'encode':
        encode_image(args.input, args.output, args.message)
    elif args.command == 'decode':
        decode_image(args.input)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
