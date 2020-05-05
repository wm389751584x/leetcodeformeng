class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        res = []
        for part in parts:
            if part:
                if part not in ('.', '..'):
                    res.append(part)
                elif part == '..' and res:
                    res.pop()
        if not res:
            return '/'
        res.insert(0, '')
        return '/'.join(res)


if __name__ == "__main__":
    s = Solution()
    assert s.simplifyPath("/home//foo/") == "/home/foo"