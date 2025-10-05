#https://leetcode.com/problems/jump-game-ii/
# Time:O(n)
# medium
# # Space:O(n)





class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1
        sc = 0
        while goal>=0:
            if goal==0:
                return sc
            else:
                for i,v in enumerate(nums[:goal]):
                    if i+v>=goal:
                        goal = i
                        sc+=1
                        break
        return sc            
            
            