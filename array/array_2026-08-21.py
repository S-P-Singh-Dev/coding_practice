# Product of Array Except Self
# Difficulty: Medium
# Topic: Array
# Time: O(n) | Space: O(1) (output array ignored)
#
# Approach:
# Use two passes: one to calculate the prefix product and another for the suffix product. Store results in an output array.
#
# Solution:

def product_except_self(nums):
    length = len(nums)
    output = [1] * length

    # Calculate prefix products
    prefix = 1
    for i in range(length):
        output[i] = prefix
        prefix *= nums[i]

    # Calculate suffix products
    suffix = 1
    for i in range(length - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]

    return output
