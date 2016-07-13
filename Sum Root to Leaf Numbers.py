# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.lt = []
    def dfs(self,root,tmp):
        if root.left == None and root.right == None:
            tmp = tmp + str(root.val)
            self.lt.append(tmp)
            return
        tmp = tmp + str(root.val)
        if root.left !=None:
            self.dfs(root.left,tmp)
        if root.right !=None:
            self.dfs(root.right,tmp)
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if(root == None):
            return 0
        tmp = ""
        self.dfs(root,tmp)
        ret = 0
        for i in self.lt:
            ret += int(i)
        return ret