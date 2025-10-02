#hhttps://leetcode.com/problems/water-bottles-ii/description/?envType=daily-question&envId=2025-10-02
# Time:O(n)
# 
# # Space:O(n)


class Solution:
    def maxBottlesDrunk(self, fullBottles: int, exchangeRate: int) -> int:
        totalDrank = 0
        emptyBottles = 0
        
        while True:
            if fullBottles > 0:
                totalDrank += fullBottles
                emptyBottles += fullBottles
                fullBottles = 0
            
            while emptyBottles >= exchangeRate:
                fullBottles += 1
                emptyBottles -= exchangeRate
                exchangeRate += 1
            
            if fullBottles == 0:
                return totalDrank