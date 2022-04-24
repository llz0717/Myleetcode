class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack,ans=[root],deque([])
        
        while stack:
            cur=stack.pop()
            if cur:
                ans.appendleft(cur.val)
                stack.append(cur.left)
                stack.append(cur.right)
        return ans
        
