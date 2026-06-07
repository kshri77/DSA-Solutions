class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        boolcandy = [False] * len(candies)
        for k,i in enumerate(candies):
            if all(i+extraCandies >= j for j in candies):
                boolcandy[k]=True
            
        return boolcandy
        