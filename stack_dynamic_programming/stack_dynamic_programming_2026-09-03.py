# Longest Valid Parentheses
# Difficulty: medium
# Topic: Stack, Dynamic Programming
# Time: O(n) | Space: O(n)
#
# Approach:
# Use a stack to track indices of unmatched '(' and the last matched ')'. For each character, if it's '(', push its index; if it's ')', pop the index from the stack and calculate the length from the current index to the popped index. Update the maximum length found.
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
