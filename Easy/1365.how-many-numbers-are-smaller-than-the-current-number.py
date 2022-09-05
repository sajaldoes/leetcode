'''
Author: Sajal Das [@sajaldoes]
Date: 2022-09-05 13:31:15
LastEditTime: 2022-09-05 14:05:45
'''
#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sort = sorted(nums)
        mapping = {}
        ans = []

        for i in range(len(nums_sort)):
            if nums_sort[i] not in mapping:
                mapping[nums_sort[i]] = i
        
        return [mapping[i] for i in nums]

        
# @lc code=end

