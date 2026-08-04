# Subarray Sum Equals K
# Difficulty: Medium
# Topic: Array, Hash Table, Prefix Sum
# Time: O(n) | Space: O(n)
#
# Approach:
# Utilize a hash map to store the cumulative sum of elements. Iterate through the array while calculating the cumulative sum, and for each sum, check if the difference between the current cumulative sum and K exists in the map. If it does, increase the count of valid subarrays.
#
# Solution:

def subarraySum(nums, k):
    count = 0
    cum_sum = 0
    sum_map = {0: 1}
    for num in nums:
        cum_sum += num
        if (cum_sum - k) in sum_map:
            count += sum_map[cum_sum - k]
        sum_map[cum_sum] = sum_map.get(cum_sum, 0) + 1
    return count
