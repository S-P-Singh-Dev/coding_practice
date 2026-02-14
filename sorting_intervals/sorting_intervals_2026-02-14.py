# Merge Intervals
# Difficulty: Medium
# Topic: Sorting, Intervals
# Time: O(n log n) | Space: O(n)
#
# Approach:
# Sort the intervals based on the starting point. Iterate through the sorted intervals and merge them if they overlap. Otherwise, add the interval to the result list.
#
# Solution:

def merge(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        last_merged = merged[-1]
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged.append(current)
    return merged
