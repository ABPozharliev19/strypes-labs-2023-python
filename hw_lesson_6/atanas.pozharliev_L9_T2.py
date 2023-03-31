import sys

file_input = sys.argv[1]
word = sys.argv[2]

with open(file_input, "r+") as f:
    lines = f.readlines()
    dic = dict()

    for i in lines:
        [key, value] = i.split(":")
        dic[key] = value

print(dic[word])
