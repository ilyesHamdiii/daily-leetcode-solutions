#https://leetcode.com/problems/replace-non-coprime-numbers-in-array/?envType=daily-question&envId=2025-09-16
# Time:O(N 2Logm)
# 
# # Space:O(n)
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        i = 0 
        while i < len(nums)-1:
            a = nums[i]
            b = nums[i+1]
            gcd = math.gcd(a, b)
            if 1 == gcd:
                i+=1
            else:
                lcm = (a*b)//gcd
                nums.pop(i)
                nums.pop(i) # removes next int as index changed
                nums.insert(i, lcm)
                if i > 0:
                    i-=1
        return nums

        
        