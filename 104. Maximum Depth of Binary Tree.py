# one line code:
# return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=[root]
        ans=0
        while q:
            tq=[]
            for n in q:
                if n.left:
                    tq.append(n.left)
                
                if n.right:
                    tq.append(n.right)
            
            q=tq
            ans+=1
        return ans
      
      
      
