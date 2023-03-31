text = input()
key = input()

if len(key) < len(text):
    key = key * (len(text) // len(key))

    key = key + key[:len(text) % len(key)]

res = ""
start = ord('a')
for l, k in zip(text, key):
    shift = ord(k) - start
    pos = start + (ord(l) - start + shift) % 26
    res += chr(pos)

print(res)