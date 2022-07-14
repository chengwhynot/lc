#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) -1
        while i <= j:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i+=1
            j-=1
# @lc code=end

