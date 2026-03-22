class Solution(object):
    def bitwiseComplement(self, n):
        binary=bin(n)[2:]
        flipped=""
        for i in binary:
            if i=='0':
                flipped+='1'
            else:
                flipped+='0'

        res=int(flipped, 2)
        return res