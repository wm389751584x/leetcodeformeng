""" Given a string, find the length of the longest substring without repeating
    characters."""

""" Example 1:

    Input: "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3. """

""" Example 2:

    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1."""

""" Example 3:

    Input: "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence
             and not a substring."""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {}
        start, max = 0
        for i in range(len(s)):
            if s[i] in lookup and lookup.get(s[i]) >= start:
                start = lookup.get(s[i]) + 1

            lookup[s[i]] = i
            max = max(max, i - start + 1)
        return max
