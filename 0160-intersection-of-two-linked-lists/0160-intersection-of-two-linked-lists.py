# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = set()
        
        tmp = headA
        while tmp:
            a.add(tmp)
            tmp = tmp.next
        
        temp = headB
        while temp:
            if temp in a:
                return temp
            temp = temp.next
        
        return None