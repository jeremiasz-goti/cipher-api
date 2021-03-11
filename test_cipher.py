from cipher import encode, decode

phrase = "(T4stowa Fr&z@]"
shifted = "čY9xytBfĀKwċEěĞ"
shift = 5

def test_encode_phrase_with_special():
    assert encode(phrase, shift) == shifted

def test_decode_phrase_with_special():
    assert decode(shifted, -abs(shift)) == phrase

def test_encode_none():
    assert encode("", shift) == ""

def test_decode_none():
    assert decode("", shift) == ""

def test_encode_space():
    assert encode(" ", shift) == "Ā"

def test_decode_space():
    assert decode("Ā", shift) == " "