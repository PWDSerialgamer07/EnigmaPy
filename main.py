import os
import random
import string
import pyperclip
# Function to clear the terminal screen


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to generate a random key


def generate_key():
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=24))
    return key

# Function to encode the text using the key


def encode_text(text, key):
    encoded_text = ''
    key_index = 0
    for char in text:
        encoded_char = chr(ord(char) ^ ord(key[key_index]))
        # Convert to hexadecimal
        encoded_text += encoded_char.encode('utf-8').hex()
        key_index = (key_index + 1) % len(key)
    return encoded_text

# Function to decode the text using the key


def decode_text(text, key):
    decoded_text = ''
    key_index = 0
    # Process two characters at a time (hexadecimal representation)
    for i in range(0, len(text), 2):
        hex_char = text[i:i+2]
        decoded_char = chr(int(hex_char, 16) ^ ord(key[key_index]))
        decoded_text += decoded_char
        key_index = (key_index + 1) % len(key)
    return decoded_text

# Function to display the main menu


def display_menu():
    clear_screen()
    print("===== Encoder/Decoder App =====")
    print("1. Decode")
    print("2. Encode")
    print("3. About")
    print("4. Exit")

# Function to handle the encoding process


def encode_menu():
    clear_screen()
    print("===== Encoding Menu =====")
    mouse_movement = input(
        "Move your mouse randomly and press Enter to generate a random key: ")
    key = generate_key()

    clear_screen()
    print("===== Encoding Menu =====")
    print("Generated Key:", key)
    text = input("Enter the text to encode: ")
    encoded_text = encode_text(text, key)

    clear_screen()
    print("===== Encoding Menu =====")
    print("Generated Key:", key)
    print("Encoded Text:", encoded_text)
    print("\n1. Copy decryption key")
    print("2. Copy result")

    while True:
        choice = input("\nEnter your choice: ")
        if choice == "1":
            pyperclip.copy(key)
            print("Decryption key copied to clipboard.")
        elif choice == "2":
            pyperclip.copy(encoded_text)
            print("Encoded text copied to clipboard.")
        elif choice == "":
            break

# Function to handle the decoding process


def decode_menu():
    clear_screen()
    print("===== Decoding Menu =====")
    key = input("Enter the decryption key: ")
    text = input("Enter the text to decode: ")
    decoded_text = decode_text(text, key)

    clear_screen()
    print("===== Decoding Menu =====")
    print("Decryption Key:", key)
    print("Decoded Text:", decoded_text)
    input("Press Enter to continue...")

# Function to display the about information


def display_about():
    clear_screen()
    print("===== About =====")
    print("Made with love, by PWDSerialgamer07(Serial)")
    input("Press Enter to continue...")


# Main program loop
while True:
    display_menu()
    choice = input("\nEnter your choice: ")

    if choice == "1":
        decode_menu()
    elif choice == "2":
        encode_menu()
    elif choice == "3":
        display_about()
    elif choice == "4":
        clear_screen()
        break
