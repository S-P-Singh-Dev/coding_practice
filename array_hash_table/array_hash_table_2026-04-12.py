# Longest Consecutive Sequence
# Difficulty: Medium
# Topic: Array, Hash Table
# Time: O(n) | Space: O(n)
#
# Approach:
# Use a hash set for O(1) average time complexity lookups. For each number, check if it's the start of a sequence (i.e., number - 1 is not in the set). Count consecutive numbers starting from the current number and update the maximum length found.
#
# Solution:

def longest_consecutive(nums):
    num_set = set(nums)
    max_length = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            max_length = max(max_length, current_length)
    return max_length
