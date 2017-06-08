def encrypt(message, key):
    from helpers import rotate_character, alphabet_position
    encoded_message = ''
    i = 0
    for char in message:
        if char.isalpha() == True:
            new_char = rotate_character(char, alphabet_position(key[i % len(key)]))
            i += 1
        else:
            new_char = char
        encoded_message += new_char
    return encoded_message

def check_key(key):
    for char in key:
        if char.isalpha() == False:
            print('Error: Key must only contain letters')
            exit()

def main():
    from sys import argv, exit
    if len(argv) == 2:
        key = argv[1]
        check_key(key)
        message = input('Type a message:\n')
    else:
        message = input('Type a message:\n')
        key = input('Encryption key:\n')
        check_key(key)
    print(encrypt(message, key))
    #print(encrypt('Shub-Niggurath: The Black Goat of the Woods with a Thousand Young', 'lovecraft'))
    #print(encrypt('Hello, world!', 'goodbye'))

if __name__ == '__main__':
    main()
