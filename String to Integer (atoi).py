class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        if len(str) == 0:
            return 0
        max_int = 2147483647
        min_int = -2147483648
        positive = True

        pos=0
        ch = str[0:1]
        if ch == '+':
            pos = 1
        if ch == "-":
            pos = 1
            positive = not positive

        ret = 0
        for ch in str[pos:]:
            if not ch.isdigit():
                break
            if positive:
                ret = ret*10 + int(ch)
                if ret > max_int:
                    return max_int
            else:
                ret = ret*10 + int(ch)
                if -ret < min_int:
                    return min_int
        if positive:
            return ret
        else:
            return -ret