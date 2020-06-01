class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        string = str.split()
        d = dict()
        if len(string) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in d:
                if string[i] in d.values():
                    return False
                d[pattern[i]] = string[i]
            elif d[pattern[i]] != string[i]:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.wordPattern("abba", "dog cat cat dog") == True