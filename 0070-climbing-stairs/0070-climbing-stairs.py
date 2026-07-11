class Solution(object):
    def climbStairs(self, n):
        f, s = 1, 1

        for _ in range(n):
            f, s = s, f + s
            
        return f