"""
925. 长按键入
你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。

你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。

 

示例 1：

输入：name = "alex", typed = "aaleex"
输出：true
解释：'alex' 中的 'a' 和 'e' 被长按。
示例 2：

输入：name = "saeed", typed = "ssaaedd"
输出：false
解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
示例 3：

输入：name = "leelee", typed = "lleeelee"
输出：true
示例 4：

输入：name = "laiden", typed = "laiden"
输出：true
解释：长按名字中的字符并不是必要的。
 

提示：

name.length <= 1000
typed.length <= 1000
name 和 typed 的字符都是小写字母。

链接：https://leetcode-cn.com/problems/long-pressed-name
"""
import itertools


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if set(name) != set(typed):
            return False

        n_len = len(name)
        t_len = len(typed)
        next_j = 0
        for i in range(n_len):
            same_word = False
            for j in range(next_j, t_len):
                if name[i] == typed[j]:
                    same_word = True
                    next_j = j + 1
                    break
                elif j > 0 and typed[j] == typed[j - 1]:
                    continue
                else:
                    return False

        return same_word

    def isLongPressedName2(self, name, typed):
        """
        方法一： 按块分组
        思路和算法

        对于字符串 S = 'aabbbbccc'，
        可以把表示成这种分组形式 - groupify(S) = [('a', 2), ('b', 4), ('c', 3)]，其中 'abc' 为 键值，[2, 4, 3] 为 连续出现的次数。

        对于一个长按键入的 typed 来说，依次每个字母连续出现的次数一定大于等于 name 中连续字母出现的次数。

        举个例子，'aaleex' 是 'alex' 其中一种长按键入的名字：
        首先把它们分别变成 [('a', 2), ('l', 1), ('e', 2), ('x', 1)] 和 [('a', 1), ('l', 1), ('e', 1), ('x', 1)] 的形式，
        这两个字符串的键值都是 'alex'，同时 [2,1,2,1] 也分别大于 [1,1,1,1]（(2 >= 1, 1 >= 1, 2 >= 1, 1 >= 1)）。

        :param name:
        :param typed:
        :return:
        """
        g1 = [(k, len(list(grp))) for k, grp in itertools.groupby(name)]
        g2 = [(k, len(list(grp))) for k, grp in itertools.groupby(typed)]
        if len(g1) != len(g2):
            return False

        return all(k1 == k2 and v1 <= v2 for (k1,v1), (k2,v2) in zip(g1, g2))




s = Solution()
name = "alex"
typed = "aaleex" # true

# name = "saeed"
# typed = "ssaaedd" # false

# name = "leelee"
# typed = "lleeelee" # true

# name = "laiden"
# typed = "laiden" # true

name =  "kikcxmvzi"
typed = "kiikcxxmmvvzz" # false

name = "saeedi"
typed =  "ssaaeediixxxiii"
print(s.isLongPressedName(name, typed))
print(s.isLongPressedName2(name, typed))