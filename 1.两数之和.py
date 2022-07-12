#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for (i, n) in enumerate(nums):
            r = target - n
            if(r in dict):
                return [dict[r], i]
            dict[n] = i
        return [-1, -1]
# @lc code=end

