class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        while num !=0:
            if num == 1:
                break
            if num %4 != 0:
                return False
            num /=4
        return True