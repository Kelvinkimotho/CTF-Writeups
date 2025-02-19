def hex_to_ascii(hex_string):
    # Split the input string into individual hex values
    hex_values = hex_string.split()
    # Convert each hex value to its corresponding ASCII character
    ascii_characters = [chr(int(h, 16)) for h in hex_values]
    # Join the characters into a single string
    return ''.join(ascii_characters)

def main():
    # user for input
    user_input = input('Enter the hex string (e.g., "0x70 0x69 ..."): ')
    # Convert the hex string to ASCII
    result = hex_to_ascii(user_input)
    print('Converted ASCII:', result)

if __name__ == '__main__':
    main()
