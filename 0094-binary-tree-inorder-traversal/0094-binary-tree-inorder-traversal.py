class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        current = root
        while current:
            if not current.left:
                result.append(current.val)
                current = current.right  # Move right
            else:
                pre = current.left
                while pre.right and pre.right != current:
                    pre = pre.right         
                if not pre.right:
                    pre.right = current  # Create a temporary link
                    current = current.left
                else:
                    pre.right = None  # Remove the temporary link
                    result.append(current.val)
                    current = current.right
        return result
