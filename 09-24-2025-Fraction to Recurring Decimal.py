#https://leetcode.com/problems/fraction-to-recurring-decimal/description/?envType=daily-question&envId=2025-09-24
# Time:O(n)
# 
# # Space:O(n)




class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []

        # Handle sign
        if (numerator > 0) ^ (denominator > 0):
            result.append("-")

        num, den = abs(numerator), abs(denominator)

        # Integer part
        result.append(str(num // den))
        remainder = num % den

        if remainder == 0:
            return "".join(result)

        result.append(".")
        remainder_map = {}

        while remainder != 0:
            if remainder in remainder_map:
                index = remainder_map[remainder]
                result.insert(index, "(")
                result.append(")")
                return "".join(result)

            remainder_map[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // den))
            remainder %= den

        return "".join(result)