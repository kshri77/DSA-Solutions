class Solution(object):
    def hasAllCodes(self, s, k):
        seen = set()
        for i in range(len(s) - k + 1):
            seen.add(s[i:i+k])
       
        total = pow(2, k)
        
        return len(seen) == total