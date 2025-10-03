#https://leetcode.com/problems/climbing-stairs/description/?envType=study-plan-v2&envId=top-interview-150
# 
# # Space:O(n)



# 3. DP Bottom-up (Tabulation)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]