# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 이전 노드를 저장할 변수
        prev_node = None
        # 현재 노드를 가르킬 변수
        current_node = head
        
        while current_node:
            next_node = current_node.next # 현재 노드 연결 끊기 전 다음 노드 지정
            current_node.next = prev_node # 현재 노드 연결 끊기(새로운 연결).
            prev_node = current_node      # 새로운 노드에 현재 노드 저장
            current_node = next_node      # 다음 노드를 현재 노드로 변경
            
        return prev_node
            
            
            