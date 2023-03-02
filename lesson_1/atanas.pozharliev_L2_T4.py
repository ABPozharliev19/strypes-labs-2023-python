import sys


def get_distinct(nums: list):
    distinct = {}

    for i in nums:
        distinct[i] = None  # Placeholder value, could be whatever

    return distinct.keys()


numbers = sys.argv[1:]

print(get_distinct(numbers))
