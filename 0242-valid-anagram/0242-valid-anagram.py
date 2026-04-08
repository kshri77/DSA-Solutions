class Solution(object):
    def isAnagram(self, s, t):
        stemp=sorted(s)
        ttemp=sorted(t)
        return stemp==ttemp