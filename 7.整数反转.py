#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#1534236469\n0

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        ## python3中不是‘/’而是‘//’。另外，python3 // 会向下取整
        # 所以 用了一下abs，以及 int_min // 10 之后要+1
        # 不是很理解为什么只要INT_MIN/MAX // 10 与res比大小就可以，不用再去判断更多一位是什么
        
        INT_MIN, INT_MAX = -2**31 -1, 2**31
        ans = 0
        minus = True if x < 0 else False
        x = abs(x)
        while (x != 0):
            if ans < INT_MIN // 10 +1 or ans > INT_MAX //10:
                return 0
            y = x % 10
            ans = ans * 10 + y
            x = x //10
        ans = -ans if minus else ans
        return ans        
# @lc code=end

