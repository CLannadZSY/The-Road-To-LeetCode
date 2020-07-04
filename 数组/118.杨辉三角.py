"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

链接: https://leetcode-cn.com/problems/pascals-triangle/
"""
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        nums = []
        for i in range(numRows):
            nums.append([1]* (i+1))
        if numRows > 2:
            for i in range(2, numRows):
                for j in range(1, i):
                    nums[i][j] = nums[i-1][j-1] + nums[i-1][j]
        return nums


if __name__ == '__main__':

    x = Solution()
    a = 10

    print(x.generate(a))
