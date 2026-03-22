class Solution(object):
    def maxSubarraySumCircular(self, nums):
        res1,res2,minEnding,maxending=nums[0],nums[0],nums[0],nums[0]
        total=nums[0]
        for i in range(1,len(nums)):
            maxending=max(maxending+nums[i],nums[i])
            minEnding = min(minEnding + nums[i], nums[i])
            res1=max(res1,maxending)
            res2=min(minEnding,res2)
            total += nums[i]

        if res1 < 0:
            return res1
        return max(res1,total-res2)
        
        