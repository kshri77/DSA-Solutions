class Solution(object):
    def subarraySum(self, nums, k):
        prefix_xor=0
        xor_map={0:1}
        count=0
        for num in nums:
            prefix_xor+=num
            target=prefix_xor-k
            count+=xor_map.get(target,0)
            xor_map[prefix_xor]=xor_map.get(prefix_xor,0)+1
        return count