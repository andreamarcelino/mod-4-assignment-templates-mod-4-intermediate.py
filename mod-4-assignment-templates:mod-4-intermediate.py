'''Module 3: Individual Programming Assignment 1
Andrea Nicole Marcelino

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    if letter == " ":
        return " "
    else:
        letter_index = ord(letter) - ord("A")
        shifted_index = (letter_index + shift) % 26
        shifted_letter = chr(shifted_index + ord("A"))
        return shifted_letter

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    shifted_message = ""
    
    for letter in message:
        index = uppercase_letters.index(letter)
        new_index = (index + shift) % len(uppercase_letters)
        shifted_message += uppercase_letters[new_index]
        
    return shifted_message

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    if letter == " ":
        return " "

    shift_number = ord(letter_shift) - 65
    letter_number = ord(letter) - 65
    shifted_number = (letter_number + shift_number) % 26
    shifted_character = chr(shifted_number + 65)
    
    return shifted_character

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    key = key * ((len(message) // len(key)) + 1)
    key = key[:len(message)] 
    
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    shifted_message = ""
    
    for i in range(len(message)):
        if message[i] == " ":
            shifted_message += " "
        else:
            message_index = uppercase_letters.index(message[i])
            key_index = uppercase_letters.index(key[i])
            encoded_index = (message_index + key_index) % len(uppercase_letters)
            shifted_message += uppercase_letters[encoded_index]
            
    return shifted_message
