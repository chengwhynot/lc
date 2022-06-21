#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
from ctypes import sizeof


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left =0 
        right = len(nums)-1
        while(left<=right):
            tmp = nums[left] + nums[right]
            if(tmp == target):
                return [left,right]
            elif(tmp < target):
                left = left +1
            elif (tmp > target):
                right = right -1
        return [-1,-1]

# @lc code=end

