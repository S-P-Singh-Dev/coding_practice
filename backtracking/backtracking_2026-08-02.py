# Permutations
# Difficulty: Medium
# Topic: Backtracking
# Time: O(n * n!) | Space: O(n)
#
# Approach:
# Use backtracking to explore all possible permutations by swapping elements. If the current index equals the length of the list, add the current permutation to the result. Swap back to undo the change for the next iteration.
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
