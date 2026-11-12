# Subsets II
# Difficulty: Medium
# Topic: Backtracking
# Time: O(2^n) | Space: O(n)
#
# Approach:
# Use backtracking to explore all subsets, skipping duplicates by sorting the input array.
#
# Solution:

from typing import List

def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    def backtrack(start, current):
        result.append(current[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result
