

def pow(n, power):
    if power == 1:
        return n

    return n * pow(n, power - 1)

print(pow(3, 2))