# Largest Rectangle in Histogram
# Difficulty: Medium
# Topic: Stack, Array
# Time: O(n) | Space: O(n)
#
# Approach:
# Use a stack to store the indices of the histogram bars. Iterate through the bars, and for each bar, pop from the stack and calculate the area when encountering a bar that is shorter than the bar at the index stored on the top of the stack.
#
# Solution:

def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0)
    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    return max_area
