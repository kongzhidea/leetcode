class Node:
    def __init__(self, p,x):
        self.val = x
        self.pos = p
    def __str__(self):
        return "[val=%d,pos=%d]"%(self.val,self.pos)

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        nodes = []
        for i,n in enumerate(num):
            nodes.append(Node(i + 1,n))
        nodes.sort(self.cmp0)
        st = 0;ed = len(nodes) - 1
        while st < ed:
            sum = nodes[st].val + nodes[ed].val
            if sum == target:
                return (min(nodes[st].pos,nodes[ed].pos),max(nodes[st].pos,nodes[ed].pos))
            if sum < target:
                st +=1
            else:
                ed -=1

    def cmp0(self,x,y):
        return cmp(x.val,y.val)