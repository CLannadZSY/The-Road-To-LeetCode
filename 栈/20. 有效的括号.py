"""
20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例2:

输入: "()[]{}"
输出: true
示例3:

输入: "(]"
输出: false
示例4:

输入: "([)]"
输出: false
示例5:

输入: "{[]}"
输出: true

链接：https://leetcode-cn.com/problems/valid-parentheses
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """栈"""
        dic = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if char in dic:
                top_element = stack.pop() if stack else ''
                if dic[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack

    def isValid2(self, s):
        """???"""
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''
