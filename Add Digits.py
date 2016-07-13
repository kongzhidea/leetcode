class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        det = num % 9
        return 9 if det == 0 else det