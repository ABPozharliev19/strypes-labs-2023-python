import sys


def power(number, exponent):
    if exponent == 0:
        return 1
    else:
        return number * power(number, exponent - 1)


number = int(sys.argv[1])
exponent = int(sys.argv[2])

print(power(number, exponent))
