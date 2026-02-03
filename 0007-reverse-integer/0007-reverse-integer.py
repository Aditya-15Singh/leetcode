class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)

        val = int(str(x)[::-1]) * sign

        if val < -2**31 or val > 2**31 - 1:
            return 0
        return val

        
        
        