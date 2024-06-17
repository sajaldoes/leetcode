'''
Author: Sajal Das
Username: sajaldoes
Date: 2022-06-21 13:59:02
LastEditTime: 2022-09-02 01:12:15
'''
#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        output = 0
        count = 0
        substring = ""
        if len(s) == 1: return 1

        for i in s:
            if i not in substring:
                count+=1
                substring+=i
            else:
                substring = i
                output = count if count>output else output
                count = 1

        output = count if count>output else output
        
        return output




        
# @lc code=end

