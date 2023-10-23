# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node.next:
            lower = min(node.val, node.next.val)
            upper = max(node.val, node.next.val)
            gcd = 0
            for i in range(1, lower+1):
                if lower % i == 0 and upper % i == 0:
                    gcd = i
                    
            node.next = ListNode(val=gcd, next=node.next)
            node = node.next.next
        return head
