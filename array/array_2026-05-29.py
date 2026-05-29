# Subarray Sum Equals K
# Difficulty: Medium
# Topic: Array
# Time: O(n) | Space: O(n)
#
# Approach:
# Use a hash map to store cumulative sums and their frequency. For each element, calculate the cumulative sum and check if the difference between the current cumulative sum and K exists in the map. Update the count of found subarrays accordingly.
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
