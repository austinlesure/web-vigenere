def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter_index = alphabet.find(letter.lower())
    return letter_index

def rotate_character(char, rotation):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if char.isalpha() == True:
        new_char_pos = (alphabet_position(char) + (rotation)) % 26
        if char.isupper() == True:
            new_char = alphabet[new_char_pos].upper()
        else:
            new_char = alphabet[new_char_pos]
    else:
        new_char = char
    return new_char
