# Permutations
# Difficulty: Medium
# Topic: Backtracking
# Time: O(n * n!) | Space: O(n)
#
# Approach:
# Utilize backtracking to generate all permutations of a given list of numbers. Swap elements in the list and recursively build permutations from the swapped positions. This ensures all possible arrangements are explored.
#
# Solution:

def permute(nums):
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]  # backtrack

    result = []
    backtrack(0)
    return result
