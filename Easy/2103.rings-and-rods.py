'''
Author: Sajal Das [@sajaldoes]
Date: 2022-09-09 10:58:31
LastEditTime: 2022-09-09 13:14:17
'''
#
# @lc app=leetcode id=2103 lang=python3
#
# [2103] Rings and Rods
#

# @lc code=start
class Solution:
    def countPoints(self, rings: str) -> int:
        # r = [0] * 10
        # g = [0] * 10
        # b = [0] * 10
        ans = 0

        # for i in range(0, len(rings), 2):
        #     if rings[i] == "R":
        #         r[int(rings[i+1])] += 1

        #     elif rings[i] == "G":
        #         g[int(rings[i+1])] += 1

        #     elif rings[i] == "B":
        #         b[int(rings[i+1])] += 1
        
        # for i in range(10):
        #     if r[i] > 0 and g[i] > 0 and b[i] > 0:
        #         ans+=1

        for i in range(10):
            i = str(i)
            if 'R'+i in rings and 'G'+i in rings and 'B'+i in rings:
                ans+=1



        return ans 
        
# @lc code=end

