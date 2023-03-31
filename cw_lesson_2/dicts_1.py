value = 'a'
d = {1:'a',2:'b',3:'c',4:'a',5:'d',6:'e',7:'a',8:'b'}
answers = []

for i in d.keys():
    if d[i] == value:
        answers.append(i)

print(answers)