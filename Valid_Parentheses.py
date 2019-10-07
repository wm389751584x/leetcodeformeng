"""Given a string containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true"""

"""
The reason to use stack is because the input value could have something like
this [{]}
So if I use my method it would be right, but it's invalid.
So by using stack we can track the most recent input.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings.This keeps the code very clean
        # Also makes adding more types of parenthesis easier
        dict = {")": "(", "}": "{", "]": "["}
        top = '#'

        for i in s:
            if i not in dict:
                top = i
                stack.append(top)
            elif top == dict[i]:
                stack.pop()
                if stack:
                    top = stack[-1]
                else:
                    top = '#'
            else:
                top = i
                stack.append(top)

        if not stack:
            return True
        else:
            return False
