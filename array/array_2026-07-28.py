# Find the Duplicate Number
# Difficulty: Medium
# Topic: Array
# Time: O(n) | Space: O(1)
#
# Approach:
# Use Floyd's Tortoise and Hare (Cycle Detection) algorithm to find the duplicate. The algorithm uses two pointers to move through the sequence and detects a cycle.
#
# Solution:

def findDuplicate(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr1
