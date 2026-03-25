class Solution(object):
    def findMiddleIndex(self, nums):
        total_sum=sum(nums)
        left=0
        for i,num in enumerate(nums):
            if left==total_sum-left-num:
                return i
            left+=num
        return -1
