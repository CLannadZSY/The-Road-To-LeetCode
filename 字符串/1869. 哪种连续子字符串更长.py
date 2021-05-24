"""
1869. 哪种连续子字符串更长
给你一个二进制字符串 s 。如果字符串中由 1 组成的 最长 连续子字符串 严格长于 由 0 组成的 最长 连续子字符串，返回 true ；否则，返回 false 。

例如，s = "110100010" 中，由 1 组成的最长连续子字符串的长度是 2 ，由 0 组成的最长连续子字符串的长度是 3 。
注意，如果字符串中不存在 0 ，此时认为由 0 组成的最长连续子字符串的长度是 0 。字符串中不存在 1 的情况也适用此规则。


示例 1：

输入：s = "1101"
输出：true
解释：
由 1 组成的最长连续子字符串的长度是 2："1101"
由 0 组成的最长连续子字符串的长度是 1："1101"
由 1 组成的子字符串更长，故返回 true 。
示例 2：

输入：s = "111000"
输出：false
解释：
由 1 组成的最长连续子字符串的长度是 3："111000"
由 0 组成的最长连续子字符串的长度是 3："111000"
由 1 组成的子字符串不比由 0 组成的子字符串长，故返回 false 。
示例 3：

输入：s = "110100010"
输出：false
解释：
由 1 组成的最长连续子字符串的长度是 2："110100010"
由 0 组成的最长连续子字符串的长度是 3："110100010"
由 1 组成的子字符串不比由 0 组成的子字符串长，故返回 false 。


提示：

1 <= s.length <= 100
s[i] 不是 '0' 就是 '1'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longer-contiguous-segments-of-ones-than-zeros
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        s += '#'
        one_str, one_str_temp = 0, 0
        zero_str, zero_str_temp = 0, 0

        for i, x in enumerate(s[:-1], 1):
            if x == '0':
                zero_str_temp += 1
            elif x == '1':
                one_str_temp += 1

            if s[i] != x:
                one_str = max(one_str_temp, one_str)
                zero_str = max(zero_str_temp, zero_str)
                zero_str_temp, one_str_temp = 0, 0

        return zero_str < one_str


S = Solution()
s = "1101"
# s = "111000"
# s = "110100010"
# s = "1000111011011010111011100101000001100001000011100111101000100100"
# s = "0"
# s = "1"  # True
print(S.checkZeroOnes(s))
