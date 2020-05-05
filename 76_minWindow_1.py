import sys, collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # return value
        res = ''
        left, right, cnt, minLen = 0, 0, 0, sys.maxsize
        tcount = collections.Counter(t)
        scount = collections.defaultdict(int)
        while right < len(s):
            scount[s[right]] += 1
            if s[right] in tcount and scount[s[right]] <= tcount[s[right]]:
                cnt += 1
            while left <= right and cnt == len(t):
                if minLen > right - left + 1:
                    minLen = right - left + 1
                    res = s[left : right + 1]
                scount[s[left]] -= 1
                if s[left] in tcount and scount[s[left]] < tcount[s[left]]:
                    cnt -= 1
                left += 1
            right += 1
        return res


if __name__ == "__main__":
    s = Solution()
    # print(s.minWindow("ADOBECODEBANC", "ABC"))
    assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"