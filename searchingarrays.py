# Built-in list (dynamic arrays)

arr = [1, 2, 3, 4, 5]

# linear search


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Binary Search(Sorted Arrays)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Binary insertion (Sorted Arrays)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# Binary deletion (Sorted Arrays)
def binary_delete(arr, target):
    index = binary_search(arr, target)
    if index != -1:
        del arr[index]
    return arr