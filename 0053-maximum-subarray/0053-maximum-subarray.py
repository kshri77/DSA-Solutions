class Solution(object):
    def maxSubArray(self, nums):
        if len(nums)==1: return nums[0]
        maxsum=float('-inf') 
        currsum=0
        for i in nums:
            currsum+=i
            if currsum>maxsum:
                maxsum=currsum
            if currsum<0:
                currsum=0
        return maxsum
            
        