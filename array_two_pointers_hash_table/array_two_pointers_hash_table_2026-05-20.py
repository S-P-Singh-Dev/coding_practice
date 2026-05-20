# 3Sum
# Difficulty: Medium
# Topic: Array, Two Pointers, Hash Table
# Time: O(n^2) | Space: O(1) (excluding the result storage)
#
# Approach:
# To find all unique triplets that sum up to zero, first, sort the array. Then, iterate through the array using a fixed index and for each index, apply the two-pointer technique to identify pairs that satisfy the sum condition.
#
# Solution:

def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return result
