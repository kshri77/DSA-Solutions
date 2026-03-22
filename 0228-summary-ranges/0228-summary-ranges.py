class Solution(object):
    def summaryRanges(self, nums):
        arr=[] 
        i=0
        while i<len(nums):
            startidx=i
            while i<len(nums)-1 and nums[i]+1==nums[i+1]:
                i+=1
            if startidx==i:
                arr.append(str(nums[i]))
            else:
                arr.append("{}->{}".format(nums[startidx], nums[i]))
            i+=1
        return arr
    