text = "hello word".replace(" ", "")
ans = {}

for ch in text:
    if ch not in ans:
        ans[ch] = 1
    else:
        ans[ch] += 1

print(ans)