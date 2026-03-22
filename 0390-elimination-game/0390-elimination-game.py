class Solution(object):
    def lastRemaining(self, n):
        rem,step,start=n,1,1
        lToR=True
        while rem>1:
            if lToR or rem%2==1:
                start+=step

            rem//=2
            step*=2
            lToR=not lToR
        return start
