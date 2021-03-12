"""

Caesar Cipher tests

"""

from cipher import encode, decode

# test data
phrase = "(T4stowa Fr&z@]"
shifted = "čY9xytBfĀKwċEěĞ"
shift = 5

# test encode method with phrase with special characters
def test_encode_phrase_with_special():
    assert encode(phrase, shift) == shifted

# test decode method with phrase with special characters
def test_decode_phrase_with_special():
    assert decode(shifted, -abs(shift)) == phrase

# test encode method with blank input
def test_encode_none():
    assert encode("", shift) == ""

# test decode method with blank input
def test_decode_none():
    assert decode("", shift) == ""

# test encode method with space as an input
def test_encode_space():
    assert encode(" ", shift) == "Ā"
#
#  test decode method with space as an input
def test_decode_space():
    assert decode("Ā", shift) == " "