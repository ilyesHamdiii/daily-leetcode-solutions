#https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/?envType=daily-question&envId=2025-10-20
# Time:O(n)
# Easy
# Space:O(n)


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for i in range(len(operations)):
            if "+" in operations[i]:
                x+=1
            else:
                x-=1
        return x
        