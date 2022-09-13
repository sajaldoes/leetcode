'''
Author: Sajal Das [@sajaldoes]
Date: 2022-09-10 21:44:32
LastEditTime: 2022-09-13 11:02:38
'''
#
# @lc app=leetcode id=832 lang=python3
#
# [832] Flipping an Image
#

# @lc code=start
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for i in range(len(image)):
            image[i] = image[i][::-1]
            for j in range(len(image)):
                image[i][j] = 1 ^ image[i][j]
        return image
# @lc code=end

