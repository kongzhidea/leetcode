class Solution(object):
    def isUgly(self, num):
        if num <=0 :
            return False
        if num in(1,2,3,4,5):
            return True
        while True:
            pre = num
            for i in (2,3,5):
                if num % i == 0:
                    num /= i
            if pre == num:
                break

        if num != 1:
            return False
        return True