import sys


def check_is_sorted(nums: list) -> bool:
    for idx, i in enumerate(nums):
        if idx == len(nums) - 1:
            break

        if i > nums[idx + 1]:
            return False

    return True


numbers = sys.argv[1:]
print(check_is_sorted(numbers))
