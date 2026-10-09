# Subarray Sum Equals K
# Difficulty: Medium
# Topic: Array / HashMap
# Time: O(n) | Space: O(n)
#
# Approach:
# Use a hashmap to keep track of the cumulative sum and its frequency. Iterate through the array, update the cumulative sum, and check if `cumulative_sum - k` exists in the hashmap to find subarrays that sum up to k.
#
# Solution:

def subarraySum(nums, k):
    count = 0
    cumulative_sum = 0
    sum_map = {0: 1}
    for num in nums:
        cumulative_sum += num
        if cumulative_sum - k in sum_map:
            count += sum_map[cumulative_sum - k]
        sum_map[cumulative_sum] = sum_map.get(cumulative_sum, 0) + 1
    return count
