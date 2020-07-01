"""
844. 比较含退格的字符串
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。

 

示例 1：

输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。
示例 2：

输入：S = "ab##", T = "c#d#"
输出：true
解释：S 和 T 都会变成 “”。
示例 3：

输入：S = "a##c", T = "#a#c"
输出：true
解释：S 和 T 都会变成 “c”。
示例 4：

输入：S = "a#c", T = "b"
输出：false
解释：S 会变成 “c”，但 T 仍然是 “b”。
 

提示：

1 <= S.length <= 200
1 <= T.length <= 200
S 和 T 只含有小写字母以及字符 '#'。
 

进阶：

你可以用 O(N) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？

链接：https://leetcode-cn.com/problems/backspace-string-compare
"""
import itertools


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        a, b = [], []
        for s in S:
            if s == '#':
                a.pop() if a else a
            else:
                a.append(s)
        for t in T:
            if t == '#':
                b.pop() if b else b
            else:
                b.append(t)

        return a == b


class Solution2(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))


x1 = Solution()
x2 = Solution2()
S = "ab#c"
T = "ad#c"
print(x1.backspaceCompare(S, T))
print(x2.backspaceCompare(S, T))
