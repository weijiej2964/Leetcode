# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        itr = head
        while itr:
            if itr.val == None:
                return True
            itr.val = None
            itr = itr.next
        return False