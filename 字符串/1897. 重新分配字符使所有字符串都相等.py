"""
1897. 重新分配字符使所有字符串都相等
给你一个字符串数组 words（下标 从 0 开始 计数）。

在一步操作中，需先选出两个 不同 下标 i 和 j，其中 words[i] 是一个非空字符串，接着将 words[i] 中的 任一 字符移动到 words[j] 中的 任一 位置上。

如果执行任意步操作可以使 words 中的每个字符串都相等，返回 true ；否则，返回 false 。



示例 1：

输入：words = ["abc","aabc","bc"]
输出：true
解释：将 words[1] 中的第一个 'a' 移动到 words[2] 的最前面。
使 words[1] = "abc" 且 words[2] = "abc" 。
所有字符串都等于 "abc" ，所以返回 true 。
示例 2：

输入：words = ["ab","a"]
输出：false
解释：执行操作无法使所有字符串都相等。


提示：

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] 由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/redistribute-characters-to-make-all-strings-equal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        from collections import Counter
        l_w = len(words)
        w = "".join(words)
        ww = Counter(w)
        for x in set(ww.values()):
            if x % l_w != 0:
                return False
        return True

        # return all([x % l_w == 0 for x in set(ww.values())])

    def makeEqual2(self, words: List[str]) -> bool:
        """
        官方解法
        """
        cnt = [0] * 26  # 每种字符的频数
        n = len(words)
        for wd in words:
            for ch in wd:
                cnt[ord(ch) - ord('a')] += 1
        return all(k % n == 0 for k in cnt)
