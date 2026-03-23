# Merge Intervals
# Difficulty: Medium
# Topic: Array, Sorting
# Time: O(n log n) due to sorting. | Space: O(n) for storing the merged intervals.
#
# Approach:
# Sort the intervals based on their start times. Iterate through each interval, merging them if they overlap. Else, add the current interval to the result list.
#
# Solution:

def merge(intervals):\n    if not intervals:\n        return []\n    intervals.sort(key=lambda x: x[0])\n    merged = []\n    current_interval = intervals[0]\n    for i in range(1, len(intervals)):\n        if intervals[i][0] <= current_interval[1]:\n            current_interval[1] = max(current_interval[1], intervals[i][1])\n        else:\n            merged.append(current_interval)\n            current_interval = intervals[i]\n    merged.append(current_interval)\n    return merged
