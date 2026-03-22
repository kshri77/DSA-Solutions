class Solution(object):
    def getHappyString(self, n, k):
        def generateString(path):
            if(len(path)==n):
                strings.append(''.join(path))
                return


            for char in ['a','b','c']:
                if not path or path[-1]!=char:
                    path.append(char)
                    generateString(path)
                    path.pop()
        strings = []
        generateString([])
        if k<=len(strings):
            return strings[k-1]
        return ""        

  
        