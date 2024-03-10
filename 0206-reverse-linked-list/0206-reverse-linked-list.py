
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
           
        def reverse(node, prev = None):
            if not node:
                return prev
            
            next, node.next = node.next, prev
            
            return reverse(next, node)
            
    
        return reverse(head)
            