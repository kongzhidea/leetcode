class Solution(object):
    def wordPattern(self, pattern, str):
        dict = {}
        rdict = {}
        ar = str.split(" ")
        if len(pattern) != len(ar):
            return False
        for i in xrange(0,len(pattern)):
            if dict.get(pattern[i]) == None:
                if rdict.get(ar[i]) != None:
                    return False
                dict[pattern[i]] = ar[i]
                rdict[ar[i]] = pattern[i]
            else:
                if dict.get(pattern[i]) != ar[i]:
                    return False
        return True