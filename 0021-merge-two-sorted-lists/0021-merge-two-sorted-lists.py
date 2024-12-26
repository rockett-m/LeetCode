# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # initialize a node for the output list - dummy
        # and a pointer - curr - for traversal
        # curr and dummy start with both pointing at the same dummy node
        curr = dummy = ListNode()
        
        # while each list has 1+ nodes left
        while list1 and list2:
            if list1.val <= list2.val:
                # set next node to ptr at node in list1
                curr.next = list1
                # advance ptr for list1 node to next node
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        # one or both of the lists have been traversed fully
        if list1:
            # append remaining list1 nodes to merged list
            curr.next = list1
        elif list2:
            curr.next = list2

        # point to start of merged list
        # this skips dummy node which was a placeholder
        return dummy.next
                