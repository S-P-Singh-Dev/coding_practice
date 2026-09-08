# Longest Consecutive Sequence
# Difficulty: Medium
# Topic: Array, Hash Table
# Time: O(n) | Space: O(n)
#
# Approach:
# Use a set to track the unique numbers. For each number, check if it's the start of a sequence and count how long the sequence goes, updating the max length found.
#
# Solution:

def longest_consecutive(nums):
    num_set = set(nums)
    max_length = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            max_length = max(max_length, current_streak)
    return max_length
