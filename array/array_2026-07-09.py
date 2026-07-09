# Product of Array Except Self
# Difficulty: Medium
# Topic: Array
# Time: O(n) | Space: O(n)
#
# Approach:
# To solve the problem without division, maintain two arrays: one for the left products and one for the right products. Calculate the running product for elements to the left and right of each index, then multiply them to get the result.
#
# Solution:

def productExceptSelf(nums):
    n = len(nums)
    left = [1] * n
    right = [1] * n
    result = [0] * n
    
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]
    
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]
    
    for i in range(n):
        result[i] = left[i] * right[i]
    
    return result
