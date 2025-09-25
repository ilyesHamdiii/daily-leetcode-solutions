#https://leetcode.com/problems/triangle/description/?envType=daily-question&envId=2025-09-25
# Time:O(n)
# 
# # Space:O(n)

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]