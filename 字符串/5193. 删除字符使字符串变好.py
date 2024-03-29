"""
5193. 删除字符使字符串变好
一个字符串如果没有 三个连续相同字符，那么它就是一个 好字符串。

给你一个字符串s，请你从 s删除最少的字符，使它变成一个 好字符串 。

请你返回删除后的字符串。题目数据保证答案总是 唯一的 。



示例 1：

输入：s = "leeetcode"
输出："leetcode"
解释：
从第一组 'e' 里面删除一个 'e' ，得到 "leetcode" 。
没有连续三个相同字符，所以返回 "leetcode" 。
示例 2：

输入：s = "aaabaaaa"
输出："aabaa"
解释：
从第一组 'a' 里面删除一个 'a' ，得到 "aabaaaa" 。
从第二组 'a' 里面删除两个 'a' ，得到 "aabaa" 。
没有连续三个相同字符，所以返回 "aabaa" 。
示例 3：

输入：s = "aab"
输出："aab"
解释：没有连续三个相同字符，所以返回 "aab" 。


提示：

1 <= s.length <= 105
s只包含小写英文字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-characters-to-make-fancy-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []

        for ch in s:
            if len(res) >= 2 and res[-1] == res[-2] == ch:
                continue

            res.append(ch)

        return "".join(res)


S = Solution()
s = "leeetcode"
print(S.makeFancyString(s))
