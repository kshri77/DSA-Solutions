class Solution(object):
    def reverseString(self, s):
        left=0
        right=len(s)-1
     
        for char in s:
            while(left<right):
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1 
        return s      