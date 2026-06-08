# Maximum Subarray
# Difficulty: Medium
# Topic: Dynamic Programming
# Time: O(n) | Space: O(1)
#
# Approach:
# Use Kadane's algorithm to find the maximum sum of a contiguous subarray in a single pass. Initialize two variables: one for the current subarray sum and another for the maximum found so far. Loop through the array, updating these variables accordingly.
#
# Solution:

def max_sub_array(nums):
    current_sum = max_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
