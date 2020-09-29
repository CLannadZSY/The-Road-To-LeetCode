"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G

链接: https://leetcode-cn.com/problems/zigzag-conversion/
许久不见, 变成 Z字转换了..
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # d = {}
        # for i in range(numRows):
        #     d[i+1] = ''
        #
        # x = 1
        # count = 1
        # change_order = False
        # for ss in s:
        #     d[abs(x)] += ss
        #
        #     if count == numRows:
        #         change_order = False if change_order else True
        #         count = 2
        #     else:
        #         count += 1
        #
        #     if not change_order:
        #         x = abs(x) if x < 0 else x
        #         x += 1
        #     else:
        #         x = -x if x > 0 else x
        #         x += 1
        #
        # return "".join(d.values())

        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows

        index, step = 0, 1

        for x in s:
            L[index] += x

            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(L)


if __name__ == '__main__':
    s = Solution()
    a = "PAYPALISHIRING"
    b = 3
    print(s.convert(a, b))
