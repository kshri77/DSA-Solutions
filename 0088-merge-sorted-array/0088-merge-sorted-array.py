class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p1,p2=m-1,n-1
        p=m+n-1
        if m==0 and n==1: nums1[0]=nums2[0]
        while(p2>=0):
            if p1>=0 and nums1[p1]>nums2[p2]:
                nums1[p]=nums1[p1]
                p1-=1
            else:
                nums1[p]=nums2[p2]
                p2-=1
            p-=1