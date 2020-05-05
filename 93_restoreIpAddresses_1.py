from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s: return []
        res = []
        self.ipaddress(s, res, [], 0)
        return res

    def ipaddress(self, s, res, temp, cnt):
        if not s:
            if cnt == 4:
                res.append('.'.join(temp))
            return
        elif cnt == 4:
            return

        self.ipaddress(s[1:], res, temp + [s[:1]], cnt + 1)
        if s[0] != '0':
            if len(s) >= 2:
                self.ipaddress(s[2:], res, temp + [s[:2]], cnt + 1)
            if len(s) >= 3 and int(s[:3]) <= 255:
                self.ipaddress(s[3:], res, temp + [s[:3]], cnt + 1)


if __name__ == "__main__":
    s = Solution()
    assert s.restoreIpAddresses("25525511135") == ["255.255.11.135", "255.255.111.35"]
    assert s.restoreIpAddresses("010010") == ["0.10.0.10","0.100.1.0"]