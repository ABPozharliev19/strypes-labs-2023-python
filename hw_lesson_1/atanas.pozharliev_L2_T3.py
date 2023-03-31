import sys


def are_distinct(nums: list) -> bool:
    distinct = {}

    for i in nums:
        if i in distinct:
            return False

        distinct[i] = 1

    return True


numbers = sys.argv[1:]

print(are_distinct(numbers))
