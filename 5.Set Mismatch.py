"""
In the Set Mismatch problem, you will be given an array of positive integers with some elements\
    missing or duplicated. You need to identify and return the missing and duplicated numbers \
        to solve this problem.

Here’s an example of the input and output values of this problem:

Input: [1, 2, 3, 4, 4, 6] | Output: [5, 4]
In this example, the missing number is 5 since it is the only positive integer from 1 to 6 that\
    is not present in the array, and the duplicate number is 4 since it appears twice.
"""


def find_error_nums(nums):
    n = len(nums)

    duplicate = -1
    for num in nums:
        if nums[abs(num) - 1] < 0:
            duplicate = abs(num)
        else:
            nums[abs(num) - 1] *= -1

    missing = -1
    for i in range(n):
        if nums[i] > 0:
            missing = i + 1
    return [duplicate, missing]


nums = [1, 2, 2, 4]
print(find_error_nums(nums))
