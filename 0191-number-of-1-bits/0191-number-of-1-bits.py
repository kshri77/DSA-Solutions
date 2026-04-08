class Solution(object):
    def hammingWeight(self, n):
        count=0
        binN=bin(n)[2:]
        for i in binN: 
            if i=='1': 
                count+=1
        return count