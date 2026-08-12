class Solution(object):
    def mergeAlternately(self, word1, word2):
        newstr=""
        for i in range(min(len(word1),len(word2))):
            newstr+=word1[i]
            newstr+=word2[i]
        remword=word1 if len(word1)>len(word2) else word2
        newstr += remword[min(len(word1), len(word2)):]
        return newstr