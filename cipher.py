"""

Caesar Cipher implementation

"""


import string

def caesar(phrase, shift):
    chars = [ x for x in string.ascii_letters + string.digits ]
    shifted = ((lambda l, n: l[n:] + l[:n])(chars, shift))
    
    msg = ""

    for i in phrase:
        if i not in chars:
            msg += i
        else:
            msg += shifted[chars.index(i)]
    
    return msg




