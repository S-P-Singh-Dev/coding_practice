# Merge Intervals
# Difficulty: Medium
# Topic: Array/Sorting
# Time: O(n log n) | Space: O(n)
#
# Approach:
# Sort the intervals based on the start time. Use a list to store merged intervals. Iterate through the sorted list and merge overlapping intervals by updating the end time of the last merged interval if they overlap.
#
# Solution:

def merge(intervals):\n    if not intervals:\n        return []\n    intervals.sort(key=lambda x: x[0])\n    merged = [intervals[0]]\n    for current in intervals[1:]:\n        last_merged = merged[-1]\n        if current[0] <= last_merged[1]:\n            last_merged[1] = max(last_merged[1], current[1])\n        else:\n            merged.append(current)\n    return merged
