class Solution(object):
    def sumGame(self, num):
        return sum([1, -1][i < len(num) / 2] * (4.5 if c == '?' else int(c)) for i, c in enumerate(num)) != 0

        
        