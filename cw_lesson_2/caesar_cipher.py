result = ""

str_in = input()
shift_in = int(input())

for ch in str_in:
    if ch == " ":
        result += " "
        continue

    if ch.isupper():
        if ord(ch) + shift_in > 90:
            result += chr(64 + 90 - abs(ord(ch) - shift_in))
        else:
            result += chr(ord(ch) + shift_in)
    else:
        if ord(ch) + shift_in > 122:
            result += chr(96 + 122 - abs(ord(ch) - shift_in))
        else:
            result += chr(ord(ch) + shift_in)

print(result)