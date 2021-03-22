"""
1796. 字符串中第二大的数字
给你一个混合字符串s，请你返回 s中 第二大 的数字，如果不存在第二大的数字，请你返回 -1。

混合字符串 由小写英文字母和数字组成。



示例 1：

输入：s = "dfa12321afd"
输出：2
解释：出现在 s 中的数字包括 [1, 2, 3] 。第二大的数字是 2 。
示例 2：

输入：s = "abc1111"
输出：-1
解释：出现在 s 中的数字只包含 [1] 。没有第二大的数字。


提示：

1 <= s.length <= 500
s只  `包含小写英文字母和（或）数字。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/second-largest-digit-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def secondHighest(self, s: str) -> int:
        s_num = {int(x) for x in s if x.isdigit()}
        nn = sorted(list(s_num))
        return nn[-2] if len(nn) > 1 else -1


S = Solution()
s = "dfa12321afd"
print(S.secondHighest(s))
