class Solution(object):
    def largestSubmatrix(self, matrix):
        res=0
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==1:
                    matrix[i][j]+=matrix[i-1][j]      

        for i in range(len(matrix)):
            matrix[i].sort(reverse=True) 
            for j in range(len(matrix[0])):
                res=max(res,matrix[i][j]*(j+1))
        return res 