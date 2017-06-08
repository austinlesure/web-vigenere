def encrypt(message, rotation):
    from helpers import rotate_character
    coded_message = ''
    for char in message:
        coded_message += rotate_character(char, rotation)
    return coded_message

def main():
    from sys import argv, exit
    message = input('Type a message:\n')
    if len(argv) == 2:
        rotation_str = argv[1]
    else:
        rotation_str = input('Rotate by:\n')
    rotation = int(rotation_str)
    print(encrypt(message, rotation))
    #print(encrypt('Hello, World!', 53))
    #print(encrypt('Walrus Love! Yay!', -1))
    #print(encrypt('Shub-Niggurath: The Black Goat of the Woods with a Thousand Young', 7))

if __name__ == '__main__':
    main()
