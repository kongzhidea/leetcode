class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        line = []
        for i in range(nRows):
            line.append([])
        up = False
        r = 0;
        for ch in s:
            if not up:
                line[r].append(ch)
                if r < nRows -1:
                    r +=1
                else:
                    r -=1
                    up = True
                continue
            if up:
                line[r].append(ch)
                if r == 0:
                    r += 1
                    up = False
                else:
                    r -=1
                continue
        return "".join(["".join(l) for l in line])