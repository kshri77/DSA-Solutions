class Solution(object):
    def checkSubarraySum(self, nums, k):
        map={0:-1}
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            rem=((total%k)+k)%k
            if rem in map:
                if i-map[rem]>=2:
                    return True
            else:
                map[rem]=i
        return False
        