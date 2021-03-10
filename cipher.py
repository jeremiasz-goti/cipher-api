"""

Caesar Cipher implementation

"""
import string

def encode(to_encode, shift):
    encrypted = ""
    whitespaces = [ ord(x) for x in string.whitespace ]
    punctuation_chars = [ ord(x) for x in string.punctuation ]
    
    for char in to_encode:
        ascii_char = ord(char)
       

        if ascii_char in range(65,90):
            char_uni = ord(char) - 65
            char_uni += shift
            char_uni = char_uni % 26
            encrypted += chr(char_uni + 65)

        elif ascii_char in range(97,123):
            char_uni = ord(char) - 97
            char_uni += shift
            char_uni = char_uni % 26
            encrypted += chr(char_uni + 97)
        
        elif ascii_char in range(48,57):
            char_uni = ord(char) - 48
            char_uni += shift
            char_uni = char_uni % 10
            encrypted += chr(char_uni + 48)

        elif ascii_char in whitespaces:
            encrypted += char
        
        elif ascii_char in punctuation_chars:
            encrypted += char

    return encrypted

def decode(to_decode, shift):
    decrypted = ""
    whitespaces = [ ord(x) for x in string.whitespace ]
    punctuation_chars = [ ord(x) for x in string.punctuation ]
    
    for char in to_decode:
        ascii_char = ord(char)
       

        if ascii_char in range(65,90):
            char_uni = ord(char) - 65
            char_uni -= shift
            char_uni = char_uni % 26
            decrypted += chr(char_uni + 65)

        elif ascii_char in range(97,123):
            char_uni = ord(char) - 97
            char_uni -= shift
            char_uni = char_uni % 26
            decrypted += chr(char_uni + 97)
        
        elif ascii_char in range(48,57):
            char_uni = ord(char) - 48
            char_uni -= shift
            char_uni = char_uni % 10
            decrypted += chr(char_uni + 48)

        elif ascii_char in whitespaces:
            decrypted += char
        
        elif ascii_char in punctuation_chars:
            decrypted += char

    return decrypted


print(encode("Jeremiasz kuchaRski 123! {", 3))
print(decode("Mhuhpldvc nxfkdUvnl 456! {", 3))






