class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bx = bin(num)
        r = ["0","b"]
        for i in xrange(2,len(bx)):
            r.append( "0" if bx[i] == "1" else "1")
        bx = "".join(r)
        return int(bx,2)
