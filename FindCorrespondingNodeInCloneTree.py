# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3590/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

tree = [1,2,3,4,5,6,7,8,9,10]
target = 5

class Solution:
    def traverse_tree(self, cloned, target):
        if (target == cloned.val):
            return cloned.val

        retval_left = None
        if (cloned.left != None):
            retval_left = self.traverse_tree(cloned.left, target)

        retval_right = None
        if (cloned.right != None):
            retval_right = self.traverse_tree(cloned.right, target)

        if (retval_left != None):
            return retval_left
        if (retval_right != None):
            return retval_right

        return None # should never reach ideally

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        cloned_node = self.traverse_tree(cloned, target)

        return cloned_node

