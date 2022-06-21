#!/usr/bin/env/ python3
from typing import List

class solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        dict = {}
        for (i, n) in enumerate(nums):
            r = target - n
            if(r in dict):
                return [dict[r],i]
            dict[n] = i
        return [-1, -1]
