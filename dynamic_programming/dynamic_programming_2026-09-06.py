# Maximum Subarray
# Difficulty: Medium
# Topic: Dynamic Programming
# Time: O(n) | Space: O(1)
#
# Approach:
# Use Kadane's algorithm to traverse the array and keep track of the maximum sum of subarrays ending at the current index. Update the global maximum when the local maximum exceeds it.
#
# Solution:

def maxSubArray(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
