# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #start a optional, starting from the beginning and keep pushing the nodes to the right
        ans = None
        while head:
            temp = ans
            ans = head
            head = head.next
            ans.next = temp

        return ans
        