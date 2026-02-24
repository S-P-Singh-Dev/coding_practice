# Median of Two Sorted Arrays
# Difficulty: Medium
# Topic: Binary Search
# Time: O(log(min(n, m))) | Space: O(1)
#
# Approach:
# Use binary search to partition both arrays into left and right halves, ensuring that all elements in the left halves are less than or equal to those in the right halves. Adjust partitions based on comparisons until the correct partition is found.
#
# Solution:

def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    x, y = len(nums1), len(nums2)
    low, high = 0, x
    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX
        maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minX = float('inf') if partitionX == x else nums1[partitionX]
        maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minY = float('inf') if partitionY == y else nums2[partitionY]
        if maxX <= minY and maxY <= minX:
            if (x + y) % 2 == 0:
                return (max(maxX, maxY) + min(minX, minY)) / 2
            else:
                return max(maxX, maxY)
        elif maxX > minY:
            high = partitionX - 1
        else:
            low = partitionX + 1

    raise ValueError('Input arrays are not sorted.')
