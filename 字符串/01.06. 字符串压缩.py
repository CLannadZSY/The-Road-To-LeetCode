"""
01.06. 字符串压缩

字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。

示例1:

 输入："aabcccccaaa"
 输出："a2b1c5a3"
示例2:

 输入："abbccd"
 输出："abbccd"
 解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
提示：

字符串长度在[0, 50000]范围内。

链接：https://leetcode-cn.com/problems/compress-string-lcci
"""


class Solution:
    def compressString(self, S: str) -> str:
        if not S:
            return ""
        ch = S[0]
        ans = ''
        cnt = 0
        for c in S:
            if c == ch:
                cnt += 1
            else:
                ans += ch + str(cnt)
                ch = c
                cnt = 1
        ans += ch + str(cnt)
        return ans if len(ans) < len(S) else S


s = Solution()
S = "aabcccccaaa"
print(s.compressString(S))
