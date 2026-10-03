# Product of Array Except Self
# Difficulty: Medium
# Topic: Array / Prefix Product
# Time: O(n) | Space: O(1) (output array is not counted as extra space)
#
# Approach:
# Use two passes to calculate the product of all elements to the left and right of each index, then combine results. This avoids using division and keeps the space usage minimal.
#
# Solution:

def productExceptSelf(nums):
    length = len(nums)
    answer = [1] * length
    left = 1
    for i in range(length):
        answer[i] = left
        left *= nums[i]
    right = 1
    for i in range(length - 1, -1, -1):
        answer[i] *= right
        right *= nums[i]
    return answer
