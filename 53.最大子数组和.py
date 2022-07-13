#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # sum 看做是以当前节点结尾的子字符串和
        # ans 表示截至当前节点的最大和
        # sum 如果小于0，对之后的节点求最大和没有帮助，直接把sum置为0
        #     否则，sum 加上当前节点的值 i，继续累加
        # 
        # 需要理解的是只有一个 sum记录累计值是不够的，还需要有一个 ans，记录当前节点和累计值中的最大的
        # 最后只返回ans 就可以。sum只是计算中间过程用。
        # 最后 ans取 sum 和 ans的最大值。
        # 因为 sum是计算当前节点和之前之和，是要累加，还是从当前节点重新算；
        # 而 ans才是累积到当前节点的最大和。
        # 状态转移方程： f[i] = max(f[i-1] + i, i)，这个方程就体现在 sum = ...这一行
        sum, ans = 0, nums[0] 
        for i in nums:
            sum = sum + i if sum > 0 else i 
            ans = max (sum, ans)
        return ans

# @lc code=end

