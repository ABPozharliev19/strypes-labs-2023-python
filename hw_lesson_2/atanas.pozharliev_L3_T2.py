import string
import sys


def vigenere_encrypt(text, key):
    upper = string.ascii_uppercase
    key_len = len(key)
    encrypted_text = ""
    trans_list = [None] * key_len
    for i, letter in enumerate(key):
        upper_shifted = upper[(ord(letter)-65):] + upper[:(ord(letter)-65)]
        trans_list[i] = str.maketrans(upper, upper_shifted)

    for i, letter in enumerate(text):
        trans = trans_list[i % key_len]
        encrypted_text += letter.translate(trans)

    return encrypted_text


text = sys.argv[1]
key = sys.argv[2]

print(vigenere_encrypt(text, key))