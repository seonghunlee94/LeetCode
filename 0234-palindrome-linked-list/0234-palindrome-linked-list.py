# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        arr = []
        
        if not head:
            return True
        
        node = head
        
        while node is not None:
            arr.append(node.val)
            
            node = node.next
        
        # while문을 통해 pop() 사용해 비교하는 것보다 시간복잡도 측면에서 나음.        
        for i in range(len(arr) // 2):
            if arr[i] != arr[-i -1]:
                return False
            
        return True