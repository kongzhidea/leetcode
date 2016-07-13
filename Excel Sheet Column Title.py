conv = {}
conv[str(0)]  ='Z'
for i in range(26):
    conv[str(i+1)] = chr(i + 65)

class Solution:
    # @return a string
    def convertToTitle(self, num):
        ret = []
        while num != 0:
            ret.append(str(num % 26))
            if num % 26 == 0:
                num = num / 26 - 1
            else:
                num = num / 26
        ret.reverse()
        return  ''.join([conv[ch] for ch in ret])