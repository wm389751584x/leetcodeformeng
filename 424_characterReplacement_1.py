# sliding windows
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        char_cnt = [0] * 26

        win_str = 0
        max_cnt = 0
        res = 0
        
        for win_end in range(n):
            char_cnt[ord(s[win_end]) - ord('A')] += 1
            curr_cnt = char_cnt[ord(s[win_end]) - ord('A')]
            max_cnt = max(max_cnt, curr_cnt)

            while win_end - win_str - max_cnt + 1 > k:
                char_cnt[win_str] -= 1
                win_str += 1
            res = max(res, win_end-win_str+1)
        return res


if __name__ == "__main__":
    pass