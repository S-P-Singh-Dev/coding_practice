# Count Subarrays with Averages Divisible by K
# Difficulty: Medium
# Topic: Array, HashMap
# Time: O(n) | Space: O(n)
#
# Approach:
# Use a prefix sum and a hashmap to count subarrays whose averages are divisible by K. For each element, compute the prefix sum and check if the remainder when divided by K has been seen before. Count occurrences using a hashmap for efficient lookup.
#
# Solution:

def subarraysDivByK(A, K):
    prefix_sum = 0
    count = 0
    remainder_count = {0: 1}

    for num in A:
        prefix_sum += num
        remainder = prefix_sum % K
        if remainder < 0:
            remainder += K
        count += remainder_count.get(remainder, 0)
        remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

    return count
