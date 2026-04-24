# Subarray Sum Equals K
# Difficulty: Medium
# Topic: Hash Table, Array
# Time: O(n) | Space: O(n)
#
# Approach:
# Use a hashmap to store the cumulative sum at each index. For each new element, calculate the cumulative sum and check if there exists a previous cumulative sum such that the difference equals K.
#
# Solution:

def subarraySum(nums, k):
    count = 0
    cum_sum = 0
    sum_counts = {0: 1}
    
    for num in nums:
        cum_sum += num
        if cum_sum - k in sum_counts:
            count += sum_counts[cum_sum - k]
        sum_counts[cum_sum] = sum_counts.get(cum_sum, 0) + 1
    
    return count
