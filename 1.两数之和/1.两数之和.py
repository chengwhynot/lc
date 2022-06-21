#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
from ctypes import sizeof


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, n in enumerate(nums):
            dp = target - n
            if dp in dict:
                return [dict[dp], i]
            dict[n] = i
        return [-1,-1]

# @lc code=end

