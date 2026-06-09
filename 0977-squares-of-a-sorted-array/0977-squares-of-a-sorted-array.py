class Solution(object):
    def sortedSquares(self, nums):
        for i,num in enumerate(nums):
            nums[i]=num*num
        def quicksort(arr):
            if len(arr) <= 1:
                return arr

            pivot = arr[len(arr) // 2]

            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]

            return quicksort(left) + middle + quicksort(right) 
        return quicksort(nums)       