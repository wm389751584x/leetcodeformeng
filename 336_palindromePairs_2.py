from typing import DefaultDict, Hashable, List
# 枚举前缀和后缀

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        def isPalindrome(word):
            return word == word[::-1]
    
        res = []

        # for i in range(len(words)):
        #     word_index[words[i]] = i

        worddict = {word : i for i, word in enumerate(words)}

        for i, word in enumerate(words):
            for j in range(len(word)+1): # 这里+1是因为，列表切片是前闭后开区间
                tmp1 = word[:j]
                tmp2 = word[j:]
                if tmp1[::-1] in worddict and worddict[tmp1[::-1]] != i and isPalindrome(tmp2):
                    res.append([i, worddict[tmp1[::-1]]])
                if tmp2[::-1] in worddict and worddict[tmp2[::-1]] != i and isPalindrome(tmp1):
                    res.append([worddict[tmp2[::-1]], i])
        return res
                    

                
        
        return res


if __name__ == "__main__":
    s = Solution()
    s.palindromePairs(["abcd","dcba","lls","s","sssll"])
