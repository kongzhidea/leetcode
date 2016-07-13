class Solution:
    # @return an integer
    def reverse(self, x):
        sign = 1
        if x < 0:
            sign = -1
        x = abs(x)
        ret = sign * int("".join(str(x)[::-1]))
        if sign ==1:
            if ret > 2147483647:
                return 0;
            return ret
        if sign == -1:
            if ret < -2147483648:
                return 0
            return ret