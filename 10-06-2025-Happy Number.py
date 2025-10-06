#https://leetcode.com/problems/happy-number/description/?envType=study-plan-v2&envId=top-interview-150
# Time:O(n)
# medium
# # Space:O(n)
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit)**2 for digit in str(n))
        
        return n == 1