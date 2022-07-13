#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
from pickle import TRUE


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
            
        d = set()
        for i in nums:
            d.add(i)
        return len(d) != len(nums)

    # def containsDuplicate2(self, nums: List[int]) -> bool:
    #     d = dict()
    #     for i in nums:
    #         if i in d:
    #             return True
    #         else:
    #             d[i] = 1
    #     return False
# @lc code=end

