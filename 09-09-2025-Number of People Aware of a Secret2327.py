#https://leetcode.com/problems/number-of-people-aware-of-a-secret/solutions/7173294/dp-solution-top-down-approach-with-memoization/?envType=daily-question&envId=2025-09-09
# Time:O(n*forget)
# 
# # Space:O(n)
#approach
"""
states: day
function: use dp(day) as # number of people who first learn the secret on this "day"
base case: for the first person: at day==1, return 1
recursion:
f(day)=sum(f(i)) for all i where (i+delay≤day<i+forget)
At the end, the answer is the sum of f(i) for all days i such that those people are still remembering at day n:
ans=sum(f(i)) for i in [n - forget + 1 .. n]"""


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        @lru_cache(None)
        def dp(day):
            # number of people who first learn the secret on this day
            if day == 1:
                return 1
            total = 0
            # look back at possible givers
            for prev in range(max(1, day - forget + 1), day - delay + 1):
                total = (total + dp(prev)) % MOD
            return total

        # sum of all people who still remember the secret on day n
        ans = 0
        for start_day in range(n - forget + 1, n + 1):
            if start_day >= 1:
                ans = (ans + dp(start_day)) % MOD
        return ans