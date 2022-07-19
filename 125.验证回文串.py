#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
from curses.ascii import isalnum


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while(left < right):
            if (s[left].isalnum() == False):
                left+=1
                continue
            if (s[right].isalnum() == False):
                right -=1
                continue
            if(s[left].lower() != s[right].lower()):
                return False
            left +=1
            right -=1
        return True

    def isPalindrome2(self, s: str) -> bool:
        s2 = "".join(c.lower() for c in s if c.isalnum())
        return s2 == s2[::-1]

    def isPalindrome1(self, s: str) -> bool:
        s1,r1 = "",""
        for c in s:
            if c.isalnum():
                s1+=c.lower()
        
        r1 = s1[::-1]
        for i in range(len(s1)):
            if s1[i] != r1[i]:
                return False
        return True
# @lc code=end
sut = Solution()
print("\"A man, a plan, a canal: Panama\" is: " + str(sut.isPalindrome("A man, a plan, a canal: Panama")))
print("\"race a car\" is: " + str(sut.isPalindrome("race a car")))
print("\"\" is: " + str(sut.isPalindrome("")))
print("\" \" is: " + str(sut.isPalindrome(" ")))



