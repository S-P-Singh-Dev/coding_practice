# Longest Increasing Subsequence
# Difficulty: Medium
# Topic: Dynamic Programming
# Time: O(n^2) | Space: O(n)
#
# Approach:
# Use dynamic programming to maintain an array where each element at index i represents the length of the longest increasing subsequence that ends with nums[i]. Iterate through the array, updating this dp array based on previous elements.
#
# Solution:

def lengthOfLIS(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
