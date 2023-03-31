import string
import sys


def caesar_cipher(text, key):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    lower_shifted = lower[key:] + lower[:key]
    upper_shifted = upper[key:] + upper[:key]

    encrypted_text = text.translate(str.maketrans(lower + upper, lower_shifted + upper_shifted))

    return encrypted_text


inp = sys.argv[1:]

text_input = inp[0]
key_input = int(inp[1])

print(caesar_cipher(text_input, key_input))
