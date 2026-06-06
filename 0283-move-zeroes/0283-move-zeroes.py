class Solution(object):
    def moveZeroes(self, nums):
        slow=0
        if all(i!=0 for i in nums): return nums
        for fast in range(1,len(nums)):
            if nums[slow]==0:
                if nums[fast]!=0:
                    nums[slow]=nums[fast]
                    nums[fast]=0
                    slow+=1
            else:
                slow+=1
        return nums
        