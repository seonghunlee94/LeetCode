# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return
        
        odd = head
        even = head.next
        even_head = head.next
        
        while odd.next and even.next:
#             odd.next = odd.next.next
#             even.next = even.next.next
            
#             odd = odd.next
#             even = even.next
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        
        odd.next = even_head
        
        return head
        