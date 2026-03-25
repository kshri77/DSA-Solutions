class Solution(object):
    def canPartitionGrid(self, grid):
        if not grid or not grid[0]:
            return False
        
        m = len(grid)      
        n = len(grid[0])   
        total_sum = sum(sum(row) for row in grid)
        
      
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        tsum = 0
        for i in range(m - 1):
            tsum += sum(grid[i])
            if tsum == target:
                return True
        
        tsum = 0
        for j in range(n - 1):
            tsum += sum(grid[i][j] for i in range(m))
            if tsum == target:
                return True
        
        return False
