#https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
# Time:O(1)
# 
# # Space:O(n)
import random
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        x=randint(1,n-1)
        while  "0" in str(x) or "0" in str(n-x):
            x=randint(1,n-1)
        return [x,n-x]