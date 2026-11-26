# Rotate Array
# Difficulty: Medium
# Topic: Array
# Time: O(n) | Space: O(1)
#
# Approach:
# To rotate the array to the right by k steps, first normalize k by taking k modulo the length of the array. Then, reverse the entire array, followed by reversing the first k elements and the remaining elements separately.
#
# Solution:

def rotate(nums, k):
    n = len(nums)
    k = k % n
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
