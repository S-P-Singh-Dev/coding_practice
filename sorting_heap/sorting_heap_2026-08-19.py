# Kth Largest Element in an Array
# Difficulty: Medium
# Topic: Sorting, Heap
# Time: O(N log K), where N is the number of elements in the array. | Space: O(K), for storing the K largest elements in the heap.
#
# Approach:
# Use a min-heap to keep track of the top K largest elements. By maintaining a heap of size K, we can efficiently find and return the Kth largest element.
#
# Solution:

import heapq

def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1]
