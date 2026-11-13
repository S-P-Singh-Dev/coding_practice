# Find the Missing Number
# Difficulty: Medium
# Topic: Array, Bit Manipulation
# Time: O(n) | Space: O(1)
#
# Approach:
# Use the XOR operation to find the missing number. XOR all elements from 0 to n and all numbers in the array. The result will be the missing number.
#
# Solution:

def missingNumber(nums):
    n = len(nums)
    result = n
    for i in range(n):
        result ^= i ^ nums[i]
    return result
