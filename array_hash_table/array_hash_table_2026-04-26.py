# Subarray Sum Equals K
# Difficulty: Medium
# Topic: Array, Hash Table
# Time: O(N) | Space: O(N)
#
# Approach:
# Use a hash map to store the cumulative sums and their frequencies. For each element, calculate the cumulative sum and check how many times (cumulativeSum - k) has occurred before.
#
# Solution:

def subarraySum(nums, k):
    count = 0
    cumulative_sum = 0
    sum_map = {0: 1}
    for num in nums:
        cumulative_sum += num
        if (cumulative_sum - k) in sum_map:
            count += sum_map[cumulative_sum - k]
        sum_map[cumulative_sum] = sum_map.get(cumulative_sum, 0) + 1
    return count
