from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        ans = []
        # get ride of ()
        s = s[1:-1]
        n = len(s)
        
        for i in range(1, n):
            left, right = s[:i], s[i:]
            left_list = self.getNumber(left)
            right_list = self.getNumber(right)
            if left_list and right_list:
                for left_number in left_list:
                    for right_number in right_list:
                        ans.append("(" + left_number + ", " + right_number + ")")
        return ans

    def getNumber(self, num):
        decimal_list = []
        n = len(num)
        if len(num) == 1 or num[0] != '0':
            decimal_list.append(num)
        
        for i in range(1, n):
            integer, fractor = num[:i], num[i:]
            print(integer, fractor)
            if (len(integer) > 1 and integer[0] == '0') or fractor[-1] == '0':
                continue
            decimal_list.append(integer + '.' + fractor)
        return decimal_list
            

if __name__ == "__main__":
    s = Solution()
    list = s.ambiguousCoordinates("(123)")
    # print(list)