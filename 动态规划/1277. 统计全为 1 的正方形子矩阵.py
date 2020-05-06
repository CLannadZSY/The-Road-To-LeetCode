"""
1277. 统计全为 1 的正方形子矩阵

给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。

 

示例 1：

输入：matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
输出：15
解释：
边长为 1 的正方形有 10 个。
边长为 2 的正方形有 4 个。
边长为 3 的正方形有 1 个。
正方形的总数 = 10 + 4 + 1 = 15.
示例 2：

输入：matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
输出：7
解释：
边长为 1 的正方形有 6 个。
边长为 2 的正方形有 1 个。
正方形的总数 = 6 + 1 = 7.
 

提示：

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1

链接：https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones
"""
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        超时
        :param matrix:
        :return:
        """
        square_matrix = 0
        mat_dic = {(i, j): y for i, x in enumerate(matrix) for j, y in enumerate(x)}

        # 边长为 1 正方形
        square_matrix += list(mat_dic.values()).count(1)

        # 边长为 2~N 的正方形
        m = len(matrix)
        n = len(matrix[0])
        for k in range(2, m + 1):
            for x in range(0, m - k + 1):
                for y in range(0, n - k + 1):
                    if all([mat_dic[(i, j)] for i in range(x, x + k) for j in range(y, y + k)]):
                        square_matrix += 1

        return square_matrix

    def countSquares2(self, matrix: List[List[int]]) -> int:
        """
        https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones/solution/tong-ji-quan-wei-1-de-zheng-fang-xing-zi-ju-zhen-2/
        :param matrix:
        :return:
        """
        m, n = len(matrix), len(matrix[0])
        f = [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    f[i][j] = matrix[i][j]
                elif matrix[i][j] == 0:
                    f[i][j] = 0
                else:
                    f[i][j] = min(f[i][j - 1], f[i - 1][j], f[i - 1][j - 1]) + 1
                ans += f[i][j]
        return ans



s = Solution()
matrix = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
print(s.countSquares(matrix))
print(s.countSquares2(matrix))
