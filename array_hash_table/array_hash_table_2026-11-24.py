# Longest Consecutive Sequence
# Difficulty: Medium
# Topic: Array, Hash Table
# Time: O(n) | Space: O(n)
#
# Approach:
# Use a set to store the elements. For each element, check if it's the start of a sequence by ensuring the previous element is not in the set. Count the length of each sequence from that starting element.
#
# Solution:

def longest_consecutive(nums):
    if not nums:
        return 0
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak
