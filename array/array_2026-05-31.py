# Maximum Product Subarray
# Difficulty: Medium
# Topic: Array
# Time: O(n) | Space: O(1)
#
# Approach:
# Iterate through the array while keeping track of the maximum and minimum products at each position. The maximum product at the current position can be the maximum of the current number, the product of current number and max product up to previous position, or the product of current number and min product up to previous position (to handle negative numbers). Similarly, update the min product.
#
# Solution:

def maxProduct(nums):
    if not nums:
        return 0

    max_prod = min_prod = result = nums[0]

    for num in nums[1:]:
        if num < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)
        result = max(result, max_prod)

    return result
