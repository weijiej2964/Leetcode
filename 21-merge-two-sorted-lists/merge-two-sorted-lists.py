# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #create a doubly linked list w/ start and end
        #begin by adding at least one into the start/end and check for edge case (0) node
        #while list1 or list2 still have nodes:
            #find the next node (smallest node)
            #set end's next to that node
            #move end to that node

        #make sure both lists have items
        if not list1:
            return list2
        elif not list2:
            return list1

        start,end = None, None
        if list1.val <= list2.val:
            start = list1
            end = list1
            list1 = list1.next
        else:
            start = list2
            end = list2
            list2 = list2.next
        
        while list1 or list2:
            if not list2 or (list1 and list1.val <= list2.val):
                end.next = list1
                end = end.next
                list1 = list1.next
            else:
                end.next = list2
                end = end.next
                list2 = list2.next

        return start

        
