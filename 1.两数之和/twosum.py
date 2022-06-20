#!/usr/bin/env/ python3
from operator import truediv
from typing import List

class solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, n in enumerate(nums):
            dp = target - n
            if dp in dict:
                return [dict[dp], i]
            dict[n] = i
        return [-1,-1]
