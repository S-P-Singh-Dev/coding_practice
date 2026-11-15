# Longest Valid Parentheses
# Difficulty: Medium
# Topic: String, Stack
# Time: O(n) | Space: O(n)
#
# Approach:
# Use a stack to keep track of indices of the opening parentheses. When encountering a closing parenthesis, check for a corresponding opening parenthesis. If a match is found, calculate the length of the valid substring and update the maximum length accordingly.
#
# Solution:

def longestValidParentheses(s: str) -> int:
    stack = [-1]
    max_length = 0
    for i, char in enumerate(s):
        if char == '(': 
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
    return max_length
