class Solution(object):
    def mergeAlternately(self, word1, word2):
        res=[]
        for i in range(min(len(word1),len(word2))):
            res.append(word1[i])
            res.append(word2[i])
        remword=word1 if len(word1)>len(word2) else word2
        res.append(remword[min(len(word1), len(word2)):])
        return "".join(res)