'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def boundaryTraversal(self, root):
        def isLeafnode(node):
            return node.left is None and node.right is None
        def leftbound(node,res):
            if not node or isLeafnode(node):
                return 
            res.append(node.data)
            if node.left:
                leftbound(node.left,res)
            elif node.right:
                leftbound(node.right,res)
            
        def leaves(node,res):
            if not node:
                return 
            if isLeafnode(node):
                res.append(node.data)
            leaves(node.left,res)
            leaves(node.right,res)
            
            
        def rightbound(node,res):
            if not node or isLeafnode(node):
                return

            if node.right:
                rightbound(node.right,res)
            elif node.left:
                rightbound(node.left,res)
            res.append(node.data)
        
        res = []
        if not root:
            return res
        if not isLeafnode(root):
            res.append(root.data)
        
        leftbound(root.left,res)
        leaves(root,res)
        rightbound(root.right,res)
        
        
        return res