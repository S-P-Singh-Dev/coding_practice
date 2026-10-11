# Valid Parentheses
# Difficulty: Medium
# Topic: Stack
# Time: O(n) | Space: O(n)
#
# Approach:
# Use a stack to track opening parentheses. Iterate through each character; for each '(', push it onto the stack. For each ')', check if the stack is empty or if the top of the stack isn't '('. If true, return false. Finally, check if the stack is empty.
#
# Solution:

def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
