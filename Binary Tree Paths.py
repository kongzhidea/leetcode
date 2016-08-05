# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ret = []
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root == None:
            return self.ret
        self.trace(root,str(root.val))
        return self.ret

    def trace(self,node,s):
        if node.left == None and node.right == None:
            self.ret.append(s)
        if node.left != None:
            self.trace(node.left,s + "->" + str(node.left.val))
        if node.right != None:
            self.trace(node.right,s + "->" + str(node.right.val))
        