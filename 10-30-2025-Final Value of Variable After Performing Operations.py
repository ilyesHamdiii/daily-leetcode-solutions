##https://leetcode.com/problems/simple-bank-system/description/?envType=daily-question&envId=2025-10-26
# Time:O(n)
# Easy
# Space:O(n)


class Solution:
    def finalValueAfterOperations(self, ope: List[str]) -> int:
        x = 0
        for i in ope:
            if i[1]=='+' :
                x+=1
            else:
                x-=1
        return x