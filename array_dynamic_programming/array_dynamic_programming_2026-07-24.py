# Maximum Subarray
# Difficulty: Medium
# Topic: Array, Dynamic Programming
# Time: O(n) | Space: O(1)
#
# Approach:
# Utilize Kadane's Algorithm to iterate through the array, maintaining the maximum sum of subarrays ending at each index. Compare the current element with the sum of the previous subarray plus the current element to decide whether to start a new subarray or continue the existing one.
#
# Solution:

def maxSubArray(nums):
    current_sum = max_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
