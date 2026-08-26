# Longest Increasing Subsequence
# Difficulty: Medium
# Topic: Dynamic Programming
# Time: O(n^2) | Space: O(n)
#
# Approach:
# Utilize a dynamic programming array to track the length of the longest increasing subsequence up to each index. For each element, check all previous elements to see if they can extend the increasing subsequence.
#
# Solution:

def length_of_lis(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
