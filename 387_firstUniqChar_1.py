from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        res = len(s)
        for key, val in cnt.items():
            if val == 1:
                res = min(res, s.index(key))
        return res if res < len(s) else -1


if __name__ == "__main__":
    pass