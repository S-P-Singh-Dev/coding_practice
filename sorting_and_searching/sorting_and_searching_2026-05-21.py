# Kth Largest Element in an Array
# Difficulty: Medium
# Topic: Sorting and Searching
# Time: O(N log K) | Space: O(K)
#
# Approach:
# Use a min-heap to maintain the top K elements of an array. Iterate through the array, adding elements to the heap. If the heap size exceeds K, remove the smallest element. Once done, the root of the min-heap will be the Kth largest element.
#
# Solution:

import heapq

def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1]
