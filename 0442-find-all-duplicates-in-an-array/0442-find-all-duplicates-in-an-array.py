class Solution(object):
    def findDuplicates(self, nums):
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        
        sorted_items = sorted(freq.items(),
                              key=lambda x: x[1],
                              reverse=True)
        freqarr=[]
        for i in range(len(sorted_items)):
            if sorted_items[i][1]==2:
                freqarr.append(sorted_items[i][0])

        return freqarr
        
        