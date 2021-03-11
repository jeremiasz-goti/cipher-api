"""

Caesar Cipher implementation

"""
import string

chars = [ x for x in string.ascii_letters + string.digits ]
specials = [ ord(x) for x in string.whitespace + string.punctuation]
specials_repl = [ chr(x) for x in range(256,294)]

def encode(phrase, shift):
    shifted = ((lambda l, n: l[n:] + l[:n])(chars, shift))    
    msg = ""

    for i in phrase:
        if ord(i) in specials:
            special_index = specials.index(ord(i))
            msg += specials_repl[special_index]
        else:
            msg += shifted[chars.index(i)]
    
    return msg


def decode(phrase, shift):
    shifted = ((lambda l, n: l[n:] + l[:n])(chars, shift))
    msg = ""

    for i in phrase:
        if i in specials_repl:
            special_index = specials_repl.index(i)
            msg += chr(specials[special_index])
        else:
            msg += shifted[chars.index(i)]
    
    return msg

