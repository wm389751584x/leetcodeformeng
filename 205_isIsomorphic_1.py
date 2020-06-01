class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ds = dict()
        n = len(s)

        for i in range(n):
            if s[i] not in ds:
                ds[s[i]] = t[i]
            elif ds[s[i]] != t[i]:
                return False
            elif ds[s[i]] in ds.values():
                return False
        return True

assert Solution().isIsomorphic("egg", "add") == True