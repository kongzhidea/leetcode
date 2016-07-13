# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.mindep = 2147483647
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root == None:
            return 0
        self.dfs(root,1)
        return self.mindep
    def dfs(self,root,dep):
        if root.left == None and root.right == None:
            self.mindep = min(self.mindep,dep)
            return
        if root.left != None:
            self.dfs(root.left,dep + 1)
        if root.right != None:
            self.dfs(root.right,dep + 1)
        