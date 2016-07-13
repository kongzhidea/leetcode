class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1 = version1.split(".")
        v2 = version2.split(".")

        v1 = self.trimRightList(v1)
        v2 = self.trimRightList(v2)

        for i in range(min(len(v1),len(v2))):
            if self.compare(int(v1[i]),int(v2[i])) != 0:
                return self.compare(int(v1[i]),int(v2[i]))

        if len(v1) > len(v2):
            return 1
        elif len(v1) < len(v2):
            return -1
        else:
            return 0

    def trimRightList(self,list):
        ln = len(list)
        pos = -1
        for i in range(ln):
            if int(list[-(i + 1)]) !=0:
                pos = i
                break

        if pos == -1:
            return []
        return list[0:len(list) - pos]


    def compare(self,n,m):
        if n>m:
            return 1
        elif n == m:
            return 0
        else:
            return -1