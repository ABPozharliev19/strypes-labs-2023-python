import sys


def are_anagrams(str1: str, str2: str) -> bool:
    letters = {}

    if len(str1) != len(str2):
        return False

    for i in str1:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1

    for i in str2:
        if i in letters:
            letters[i] -= 1
        else:
            return False

    for value in letters.values():
        if value != 0:
            return False
    return True


words = sys.argv[1:]
word1 = words[0]
word2 = words[1]

print(are_anagrams(word1, word2))
