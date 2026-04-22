# 3Sum
# Difficulty: Medium
# Topic: Array, Two Pointers
# Time: O(n^2) | Space: O(1)
#
# Approach:
# Use sorting and two-pointer technique to find triplets that sum to zero. For each element, use two pointers to find the remaining two numbers. Skip duplicates to ensure unique triplets.
#
# Solution:

def three_sum(nums):
    nums.sort()
    triplets = []
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
                triplets.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return triplets
