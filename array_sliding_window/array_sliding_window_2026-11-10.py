# Sliding Window Maximum
# Difficulty: Medium
# Topic: Array, Sliding Window
# Time: O(n) | Space: O(k)
#
# Approach:
# Use a deque to keep track of the maximum elements' indices within the current sliding window. Remove elements that are out of the window and maintain the order in the deque.
#
# Solution:

from collections import deque

def max_sliding_window(nums, k):
    if not nums:
        return []
    result = []
    q = deque()
    for i, num in enumerate(nums):
        if q and q[0] < i - k + 1:
            q.popleft()
        while q and nums[q[-1]] < num:
            q.pop()
        q.append(i)
        if i >= k - 1:
            result.append(nums[q[0]])
    return result
