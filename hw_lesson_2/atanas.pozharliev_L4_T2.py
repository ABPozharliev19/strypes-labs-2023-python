import sys


def histogram_purity(text):
    histogram = {}
    for symbol in text:
        if symbol in histogram:
            histogram[symbol] += 1
        else:
            histogram[symbol] = 1
    return histogram


print(histogram_purity(sys.argv[1]))