"""
40. 组合总和 II

给定一个数组candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。

candidates中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。
示例1:

输入: candidates =[10,1,2,7,6,1,5], target =8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例2:

输入: candidates =[2,5,2,1,2], target =5,
所求解集为:
[
 [1,2,2],
 [5]
]

链接：https://leetcode-cn.com/problems/combination-sum-ii
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        mylist = []

        for i in range(len(candidates)):
            diff = target - candidates[i]
            if diff == 0 and [candidates[i]] not in mylist:
                mylist.append([candidates[i]])
            elif diff > 0:
                result = self.combinationSum2(candidates[i + 1:], diff)
                if result:
                    new_result = []
                    for ll in result:
                        ll.insert(0, candidates[i])
                        ll.sort()
                        if ll not in mylist:
                            new_result.append(ll)

                    mylist += new_result

        return mylist

    def combinationSum2_2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        更快
        """
        if target == 0 or len(candidates) == 0:
            return []
        result = []

        def helper(tar, idx, cur):
            if tar == 0:  # 终止条件
                result.append(cur[:])
                return
            for i in range(idx, len(candidates)):
                if candidates[i] > tar:
                    break
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                cur.append(candidates[i])
                helper(tar - candidates[i], i + 1, cur)
                cur.pop()  # 回溯记得恢复状态

        candidates.sort()
        helper(target, 0, [])
        return result


s = Solution()
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(s.combinationSum2(candidates, target))
print(s.combinationSum2_2(candidates, target))
