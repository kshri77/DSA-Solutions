class Solution(object):
    def areSimilar(self, mat, k):
        n=len(mat[0])
        m=len(mat)
        k%=n
        for r in range(m):
            if r%2==0:
                shifted = mat[r][k:] + mat[r][:k]
            else:
                shifted = mat[r][-k:] + mat[r][:-k]
            
            if shifted != mat[r]:
                return False
        return True
        