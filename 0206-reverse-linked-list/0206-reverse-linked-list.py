# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None        
        curr = head
        
        while curr:
            # store next node in temp variable
            next_node = curr.next
            # set prev seen node to be the node this points fwd to
            curr.next = prev
            # save curr as prev
            prev = curr
            # set next node to curr and advance
            curr = next_node
            
        return prev