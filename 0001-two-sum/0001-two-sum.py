class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        i=0
        for num in nums:
            diff=target-num

            if diff in seen:
                return nums.index(diff),i
            seen[num]=True
            i+=1   