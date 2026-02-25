# Find Minimum in Rotated Sorted Array
# Difficulty: Medium
# Topic: Binary Search
# Time: O(log n) | Space: O(1)
#
# Approach:
# Use binary search to efficiently find the minimum element in a rotated sorted array. Adjust the search bounds based on the mid element's comparison with the leftmost element.
#
# Solution:

def findMin(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]
