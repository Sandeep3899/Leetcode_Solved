class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  
        
        #BFS with dq
        level = 0
        dq = deque([root])

        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            level += 1
        return level
