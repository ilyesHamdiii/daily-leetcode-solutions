#https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/?envType=daily-question&envId=2025-10-25
# Time:O(n)
# Easy
# Space:O(n)

class Solution:
    def totalMoney(self, n: int) -> int:
        leftover_days = n%7
        full_weeks = n//7
        monday = 1
        cur_sum=0
        for i in range(1, full_weeks+1):
            cur_sum+= sum(range(monday, monday+7))
            monday+=1
        
        cur_sum+= sum(range(monday, monday+leftover_days))
        print(cur_sum)
        return cur_sum
            