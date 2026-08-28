# Search in Rotated Sorted Array
# Difficulty: Medium
# Topic: Binary Search
# Time: O(log n) | Space: O(1)
#
# Approach:
# We will use a modified binary search approach to find the target. First, identify which side of the array is sorted, then check if the target lies within the sorted range. Adjust the search range accordingly until we find the target or exhaust the search space.
#
# Solution:

def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
