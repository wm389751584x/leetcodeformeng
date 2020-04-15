class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        if not s: return 0

        res = lookup[s[-1]]

        for i in range(len(s)-2, -1, -1):
            if lookup[s[i]] > lookup[s[i+1]]:
                res += lookup[s[i]]
            else:
                res -= lookup[s[i]]
        
        return res


if __name__ == "__main__":
    pass