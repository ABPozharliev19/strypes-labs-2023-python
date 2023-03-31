import sys

d = {1:'a',2:'b',3:'c',4:'a',5:'d',6:'e',7:'a',8:'b'}


def find(value):
    answers = []

    for i in d.keys():
        if d[i] == value:
            answers.append(i)
    return answers


print(find(sys.argv[1]))