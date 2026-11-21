# Longest Consecutive Sequence
# Difficulty: Medium
# Topic: Array, Hash Table
# Time: O(n) | Space: O(n)
#
# Approach:
# Use a hash set to store the elements for O(1) access. For each number, check if it's the start of a sequence. If it is, count the length of the sequence by continually checking for consecutive numbers.
#
# Solution:

def longestConsecutive(nums):
    num_set = set(nums)
    longest_streak = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
    return longest_streak
