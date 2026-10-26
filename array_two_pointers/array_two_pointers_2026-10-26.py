# Two Sum II - Input Array Is Sorted
# Difficulty: Medium
# Topic: Array, Two Pointers
# Time: O(n) | Space: O(1)
#
# Approach:
# Use two pointers, one starting at the beginning and the other at the end of the array. Calculate the sum of the values pointed to by both pointers. If the sum equals the target, return the indices. If the sum is less than the target, move the left pointer up; if greater, move the right pointer down.
#
# Solution:

def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
