"""

Caesar Cipher implementation

"""

def encode(to_encode, shift):
    encrypted = ""
    for i in to_encode:
        encrypted += chr(ord(i) + shift)
    return encrypted

def decode(to_decode, shift):
    decrypted = ""
    for i in to_decode:
        decrypted += chr(ord(i) - shift)
    return decrypted

print(encode("abcd fdsa 123",3))
print(decode("defg#igvd#456", 3))