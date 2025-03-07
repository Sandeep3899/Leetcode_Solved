# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None  # Base case: return None for empty list

        mid = len(nums) // 2
        root = TreeNode(nums[mid])  # Root is the middle element
        root.left = self.sortedArrayToBST(nums[:mid])  # Recursively construct left subtree
        root.right = self.sortedArrayToBST(nums[mid+1:])  # Recursively construct right subtree

        return root  # Return root node
        