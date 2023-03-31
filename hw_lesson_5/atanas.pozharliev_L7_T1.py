class Fibs(object):
    def __init__(self):
        self.num1 = 0
        self.num2 = 1

    def __next__(self):
        temp = self.num1
        self.num1 = self.num2
        self.num2 = temp + self.num2
        return self.num2

    def __iter__(self):
        return self


fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f)
        break
