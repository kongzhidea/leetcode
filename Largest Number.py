class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num.sort(self._cmp)
        ret = "".join(map(str,num)).lstrip("0")
        if ret == "":
            return "0"
        return ret
    def _cmp(self,x,y):
        return -cmp(int(str(x) + str(y)) , int(str(y) + str(x)))