# Product of Array Except Self
# Difficulty: Medium
# Topic: Array
# Time: O(n) | Space: O(1) (output array not counted)
#
# Approach:
# Use two passes to calculate the product of all elements to the left and right of each index, then multiply those two results for each index.
#
# Solution:

def product_except_self(nums):
    length = len(nums)
    output = [1] * length

    left_product = 1
    for i in range(length):
        output[i] = left_product
        left_product *= nums[i]

    right_product = 1
    for i in range(length - 1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]

    return output
