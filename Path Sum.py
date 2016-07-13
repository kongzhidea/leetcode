# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        return self.solve(root,0,sum)

    def solve(self,root,sum,total):
        if root == None:
            return False
        if root.left == None and root.right == None:
            return sum + root.val== total
        return self.solve(root.left,sum + root.val,total) or self.solve(root.right,sum+root.val,total)
        

        