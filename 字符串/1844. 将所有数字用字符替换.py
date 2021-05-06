"""
1844. 将所有数字用字符替换

给你一个下标从 0开始的字符串 s，它的 偶数 下标处为小写英文字母，奇数下标处为数字。

定义一个函数shift(c, x)，其中c是一个字符且x是一个数字，函数返回字母表中c后面第 x个字符。

比方说，shift('a', 5) = 'f'和shift('x', 0) = 'x'。
对于每个 奇数下标i，你需要将数字s[i] 用shift(s[i-1], s[i])替换。

请你替换所有数字以后，将字符串 s返回。题目 保证shift(s[i-1], s[i])不会超过 'z'。



示例 1：

输入：s = "a1c1e1"
输出："abcdef"
解释：数字被替换结果如下：
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('c',1) = 'd'
- s[5] -> shift('e',1) = 'f'
示例 2：

输入：s = "a1b2c3d4e"
输出："abbdcfdhe"
解释：数字被替换结果如下：
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('b',2) = 'd'
- s[5] -> shift('c',3) = 'f'
- s[7] -> shift('d',4) = 'h'


提示：

1 <= s.length <= 100
s只包含小写英文字母和数字。
对所有 奇数 下标处的i，满足shift(s[i-1], s[i]) <= 'z'。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/replace-all-digits-with-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ""
        for i, ch in enumerate(s):
            if i % 2:
                res += chr(ord(s[i - 1]) + int(ch))
            else:
                res += ch

        return res


S = Solution()
s = "a1b2c3d4e"
print(S.replaceDigits(s))
