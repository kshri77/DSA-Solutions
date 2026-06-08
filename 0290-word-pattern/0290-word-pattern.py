class Solution(object):
    def wordPattern(self, pattern, s):
        string = s.split()
        if len(string)!=len(pattern): return False

        shash={}
        phash={}

        for word, pat in zip(string, pattern):
            
            if pat not in shash:
                shash[pat] = word
            elif shash[pat] != word:
                return False

            if word not in phash:
                phash[word] = pat
            elif phash[word] != pat:
                return False

        return True


        