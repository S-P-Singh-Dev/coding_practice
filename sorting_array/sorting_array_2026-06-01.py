# Merge Intervals
# Difficulty: Medium
# Topic: Sorting, Array
# Time: O(n log n) due to sorting, where n is the number of intervals. | Space: O(n) for the output list in the worst case.
#
# Approach:
# Sort the intervals based on their start times. Then, iterate through the sorted intervals and merge them if they overlap. If there's no overlap, add the current interval to the results.
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
