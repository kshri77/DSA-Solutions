class Solution(object):
    def runningSum(self, nums):
        sum=nums[0]
        for i in range(len(nums)-1):
            nums[i]=sum
            sum+=nums[i+1]
        nums[len(nums)-1]=sum
        return nums

        
        