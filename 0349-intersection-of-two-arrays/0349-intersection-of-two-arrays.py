class Solution(object):
    def intersection(self, nums1, nums2):
        intersect=[]
        num1set=set(nums1)
        for num in nums2:
            if num in num1set:
                if num not in intersect: intersect.append(num)
        return intersect