class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return[]
        ma_len = len(matrix)
        x, y = 0, 0
        a, b = ma_len - 1, ma_len - 1
        for i in range(ma_len):
            for j in range(ma_len):
                if (x+j) == (a-i) and (y+i) == (b-j):
                    break
                else:
                    matrix[x+j, y+i], matrix[a-i, b-j] = matrix[a-i, b-j], matrix[x+j, y+i]


mylist = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(Solution().rotate(mylist))