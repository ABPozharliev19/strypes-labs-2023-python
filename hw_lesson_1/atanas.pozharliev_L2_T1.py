import sys


def check_is_sorted(nums: list) -> str:
    for idx, i in enumerate(nums):
        if idx == len(nums) - 1:
            break

        if i > nums[idx + 1]:
            return "unsorted"

    return "sorted"


numbers = sys.argv[1:]
print(check_is_sorted(numbers))
