# Kth Largest Element in an Array
# Difficulty: Medium
# Topic: Sorting, Heap
# Time: O(N log k) | Space: O(k)
#
# Approach:
# 1. Utilize a min-heap of size k to store the k largest elements. 2. Traverse through each element of the array, adding it to the heap. 3. If the size of the heap exceeds k, remove the smallest element. 4. The root of the heap will be the kth largest element.
#
# Solution:

import heapq

def findKthLargest(nums, k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]
