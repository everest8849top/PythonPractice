"""
The binary search algorithm is a searching algorithm used to find an element in a\
    sorted array by repeatedly dividing the search interval in half. \
    Below is how the Binary Search algorithm works:

It starts by defining a search range that spans the entire array.
Then compares the target value with the middle element of the search range.
If the target value is equal to the middle element, the target is found and returns its index.
If the target value is less than the middle element, the algorithm discards the upper \
    half of the search range and repeats step 2 with the lower half.
If the target value is greater than the middle element, the algorithm discards the lower \
    half of the search range and repeats step 2 with the upper half.
It repeats steps 2 through 5 until the target value is found or the search range is empty.
Below is the kind of input and output you will see in the problem of binary search in your coding interviews:

Input = [-1,0,3,5,9,12], target = 9 | Output = 4
"""


def search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(search(nums, target))
