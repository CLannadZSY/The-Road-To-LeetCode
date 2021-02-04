"""
692. 前K个高频单词
给一非空的单词列表，返回前k个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。

示例 1：

输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。


示例 2：

输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
输出: ["the", "is", "sunny", "day"]
解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
    出现次数依次为 4, 3, 2 和 1 次。


注意：

假定 k 总为有效值， 1 ≤ k ≤ 集合元素数。
输入的单词均由小写字母组成。


扩展练习：

尝试以O(n log k) 时间复杂度和O(n) 空间复杂度解决。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List
from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res = []

        word_dic = defaultdict(list)
        for w in set(words):
            cnt = words.count(w)
            word_dic[cnt].append(w)

        word_key = sorted(word_dic.keys(), reverse=True)
        for key in word_key:
            word_value = sorted(word_dic[key])
            l_v = len(word_value)
            if k < l_v:
                res.extend(word_value[:k])
            else:
                res.extend(word_value)
            k -= l_v
            if k <= 0:
                break

        return res

    def topKFrequent2(self, words: List[str], k: int) -> List[str]:
        """

        """

        count = collections.Counter(words)
        heap = []
        ans = []
        for c in count.items():
            heapq.heappush(heap, (-c[1], c[0]))

        while len(ans) < k:
            tmp = heapq.heappop(heap)
            ans.append(tmp[1])

        return ans

    def topKFrequent3(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]


if __name__ == '__main__':
    S = Solution()
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is", "is"]
    k = 4
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 3
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 1
    print(S.topKFrequent(words, k))
    print(S.topKFrequent2(words, k))
