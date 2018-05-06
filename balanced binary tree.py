class TreeNode(object):
   def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None

class Solution(object):
   def isSameTree(self,p,q):
      if not p and not q: #如果两个都能最后取到没有数值的情况。
         return True
      if p and q and p.val == q.val:
         x = self.isSameTree(p.left,q.left)#p和q所有的左子节点进行比较
         y = self.isSameTree(p.right,q.right)#p和q所有的右子节点进行比较
         return x and y #当x和y都为true的时候才是true
      else:
         return False
         
      
      
       