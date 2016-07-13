class Solution(object):
    def isHappy(self, n):
        dict = {}
        dict[n] = 1
        while True:
            m = 0
            while n > 0:
                m += (n%10) * (n%10)
                n /= 10
            if m == 1:
                return True
            if dict.get(m) == 1:
                return False
            dict[m] = 1
            n = m