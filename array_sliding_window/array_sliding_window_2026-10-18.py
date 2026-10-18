# Count Subarrays with Bounded Maximum
# Difficulty: Medium
# Topic: Array, Sliding Window
# Time: O(n) | Space: O(1)
#
# Approach:
# Utilize a sliding window to count valid subarrays. Traverse the array while maintaining two pointers. Use a counter for valid subarrays where the maximum element is within bounds.
#
# Solution:

def countSubarrays(A, L, R):
    count = 0
    last_invalid = -1
    last_valid = 0
    for i, num in enumerate(A):
        if num > R:
            last_invalid = i
            last_valid = 0
        else:
            last_valid = i - last_invalid
        if num >= L:
            count += last_valid
    return count
