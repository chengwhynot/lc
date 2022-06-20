#!/usr/bin/env/ python3
from operator import truediv
from typing import List

class solutin:
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
