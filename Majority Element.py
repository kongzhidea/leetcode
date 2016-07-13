class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        count = 0;ret = 0
        for n in num:
            if count == 0:
                count += 1
                ret = n
                continue
            if n == ret:
                count += 1
            else:
                count -= 1
        return ret