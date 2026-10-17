# Longest Consecutive Sequence
# Difficulty: Medium
# Topic: Arrays & Hashing
# Time: O(n) | Space: O(n)
#
# Approach:
# Use a set to store the numbers for O(1) look-up times. Iterate through each number, and if it is the start of a sequence, continue checking for consecutive numbers to find the length of that sequence. Keep track of the maximum length found.
#
# Solution:

def longestConsecutive(nums):
    if not nums:
        return 0
    num_set = set(nums)
    max_length = 0
    for num in num_set:
        if num - 1 not in num_set:
            length = 0
            while num + length in num_set:
                length += 1
            max_length = max(max_length, length)
    return max_length
