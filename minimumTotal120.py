class Solution:
    def minimumTotal(self, triangle):
        
        length = len(triangle)
        
        
        res = [0 for i in range(length)]
        
        if not triangle:
            return 0
        
        res[0] = triangle[0][0]
        tri = 0
        
        for i in range(1, length):
            
            left = tri - 1 if (tri - 1) > 0 else 0
            right = tri + 1 if (tri + 1) < len(triangle[i]) else len(triangle[i]) - 1
            # print("right", right)
            
            if triangle[i][left] >= triangle[i][right]:
                res[i] = res[i-1] + triangle[i][right]
                tri = right
            else:
                res[i] = res[i-1] + triangle[i][left]
                tri = left
        
        return res[-1]


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

print(Solution().minimumTotal(triangle))