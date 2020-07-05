"""
119.杨辉三角II.py
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

输入: 3
输出: [1,3,3,1]

链接: https://leetcode-cn.com/problems/pascals-triangle-ii/
"""


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        nums = []
        for i in range(numRows + 1):
            nums.append([1] * (i + 1))
        if numRows + 1 > 2:
            for i in range(2, numRows + 1):
                for j in range(1, i):
                    nums[i][j] = nums[i - 1][j - 1] + nums[i - 1][j]
        return nums[numRows]


if __name__ == '__main__':
    x = Solution()
    a = 4

    print(x.generate(a))
