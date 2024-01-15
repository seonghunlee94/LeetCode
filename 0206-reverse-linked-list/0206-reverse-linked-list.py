# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         node = head
#         prev = None
        
#         while node:
#             next_node = node.next
#             node.next = prev
#             prev = node
#             node = next_node
      
#         return prev
        
    
        def reverse(node, prev = None):
            if not node:
                return prev
            
            # node.next, node, prev = prev, node.next, node
            # 다음 노드와 잘려나간 이전 노드를 활용해야 한다.
            next, node.next = node.next, prev
            
            return reverse(next, node)
            
    
        return reverse(head)
            