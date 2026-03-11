# Sliding Window Maximum
# Difficulty: Medium
# Topic: Dynamic Programming, Queue
# Time: O(n) | Space: O(k) where k is the size of the window
#
# Approach:
# Use a deque to maintain indices of useful elements in the window. For each element, remove indices that are out of the current window and those which are less than the current element as they are not needed for future max computations.
#
# Solution:

from collections import deque

def maxSlidingWindow(nums, k):
    if not nums:
        return []
    result = []
    dq = deque()
    for i in range(len(nums)):
        # Remove indices out of the current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        # Remove smaller elements as they are not useful
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        # Add the maximum for the current window
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
