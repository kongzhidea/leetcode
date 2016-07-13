class Solution(object):
    def singleNumber(self, nums):
        diff = 0
        for i in nums:
            diff = diff^i
        pos = 0
        for i in xrange(0,32):
            if diff & (1<<i) >0:
                pos = i
                break
        res = [0,0]
        print diff,pos
        for n in nums:
            if n & (1<<pos) == 0:
                res[0] ^= n
            else:
                res[1] ^= n
        return res