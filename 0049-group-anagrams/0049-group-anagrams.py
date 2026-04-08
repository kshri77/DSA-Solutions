class Solution(object):
    def groupAnagrams(self, strs):
        anagram={}
        for word in strs:
            sorted_word=''.join(sorted(word))
            if sorted_word not in anagram:
                anagram[sorted_word]=[]
            anagram[sorted_word].append(word)
        return list(anagram.values())

        