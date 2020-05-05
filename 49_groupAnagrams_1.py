from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: return []
        res = []
        lookup = dict()

        for i in range(len(strs)):
            temp = sorted(strs[i])
            temp = ''.join(temp)
            if temp in lookup:
                res[lookup[temp]].append(strs[i])
            else:
                res.append([strs[i]])
                lookup[temp] = len(res) - 1

        return res

    
if __name__ == "__main__":
    s = Solution()
    assert s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [["eat","tea","ate"],["tan","nat"],["bat"]]