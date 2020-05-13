class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        v1 = version1.split('.')
        v2 = version2.split('.')

        len_v1, len_v2 = len(v1), len(v2)
        maxlen = max(len_v1, len_v2)

        for i in range(maxlen):
            temp1, temp2 = 0, 0
            if i < len_v1:
                temp1 = v1[i]
            if i < len_v2:
                temp2 = v2[i]
            if temp1 > temp2:
                return 1
            elif temp1 < temp2:
                return -1
        return 0


if __name__ == "__main__":
    s = Solution()
    assert s.compareVersion('0.1', '1.1') == -1
