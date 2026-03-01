# Longest Consecutive Sequence
# Difficulty: Medium
# Topic: Hashing
# Time: O(n) | Space: O(n)
#
# Approach:
# Use a set to store all unique numbers, then iterate through each number. For each number, check if it is the start of a sequence (number - 1 is not in the set). If it is, count the length of the sequence by incrementing and checking successful consecutive numbers.
#
# Solution:

def longestConsecutive(nums):
    if not nums:
        return 0
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
