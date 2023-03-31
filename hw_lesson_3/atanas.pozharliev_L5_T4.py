import sys


def check_palindrome(word):
    if not word or len(word) == 1:
        return 1
    if word[0] == word[-1]:
        return check_palindrome(word[1:-1])
    return 0


word = sys.argv[1]

print(check_palindrome(word))
