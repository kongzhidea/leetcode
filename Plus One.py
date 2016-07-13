class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        ret = []
        x = 1
        for i in range(len(digits)):
            num = digits[len(digits) - i -1]
            num  = num + x
            ret.insert(0,num % 10)
            x = num / 10
        if x > 0:
            ret.insert(0,x)
        return ret