# 3Sum Closest
# Difficulty: Medium
# Topic: Array, Two Pointers
# Time: O(n^2) | Space: O(1)
#
# Approach:
# Sort the array and use a loop to fix one element and two pointers to find two more elements. Adjust pointers based on the sum compared to the target.
#
# Solution:

def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum
    return closest_sum
