#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = -1
        dt = dict()
        for c in s:
            if c not in dt:
                dt[c] = 1
            else:
                dt[c] += 1
        # print(dt) # {'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1}

        for i, n in enumerate(s):
            # print(i, n) # "0 l, 1 e, 2 t, 3 c, 4 o, 5 d",  所以不能拿n当作出现次数来判断
            if dt[n] == 1:
                return i
        return -1
# @lc code=end        

s = Solution()
r = s.firstUniqChar("abcbc")
print(r)


