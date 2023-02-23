# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        list1 = []; list2 = []

        node = l1
        while node.next != None:
            list1.append(str(node.val))
            node = node.next
        
        list1.append(str(node.val)); list1.reverse()
        int1 = ''.join(list1); int1 = int(int1)
        
        node = l2
        while node.next != None:
            list2.append(str(node.val))
            node = node.next
        
        list2.append(str(node.val)); list2.reverse()
        int2 = ''.join(list2); int2 = int(int2)
        
        summ = int1 + int2
        sum_list = []
        for i in str(summ):
            sum_list.append(int(i))


        for iter in range(len(sum_list)):
            
            node = ListNode()
            
            if iter != 0:  # next is None by default - which we want for first elem
                node.next = prev

            node.val = sum_list[iter]

            prev = node # so we can embed it

        return node