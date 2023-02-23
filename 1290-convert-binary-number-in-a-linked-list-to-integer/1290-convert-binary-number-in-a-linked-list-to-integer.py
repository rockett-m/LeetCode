# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        node = head; count = 0
        while node.next != None:
            node = node.next
            count += 1

        node = head; total = 0
        while node.next != None:
            
            if node.val != 0: # don't add zero digits
                total += pow(2, count)  # 2 ^ count
            node = node.next
            count -= 1

        # while node.next == None:  # final
        if node.val != 0: # don't add zero digits
            total += pow(2, count)  # 2 ^ count

        return total
        