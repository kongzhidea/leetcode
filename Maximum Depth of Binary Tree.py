# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def __init__(self):
        self.depth = 0
    def maxDepth(self, root):
        self.dfs(root,1)
        return self.depth
    def dfs(self,node,dp):
        if node == None:
            return
        if node.left == None and node.right == None:
            self.depth = max(self.depth,dp)
            return
        if node.left !=None:
            self.dfs(node.left,dp + 1)
        if node.right !=None:
            self.dfs(node.right,dp + 1)