def binary_search(arr, low, high, n):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == n:
            return mid
        elif arr[mid] > n:
            return binary_search(arr, low, mid - 1, n)
        else:
            return binary_search(arr, mid + 1, high, n)

    else:
        return "not in array"


print(binary_search([1, 2, 3], 0, 2, 3))
