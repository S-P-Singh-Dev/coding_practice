# 3Sum Closest
# Difficulty: Medium
# Topic: Two Pointers, Array
# Time: O(n^2) | Space: O(1)
#
# Approach:
# Sort the array and use a two-pointer technique to find the closest sum of three numbers to the target. Compute sums and track the minimum difference from the target.
#
# Solution:

def three_sum_closest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            if abs(curr_sum - target) < abs(closest_sum - target):
                closest_sum = curr_sum
            if curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                return curr_sum
    return closest_sum
