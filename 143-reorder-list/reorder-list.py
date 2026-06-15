# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #using slow and fast pointers, seperate the head into two parts (temp = s, s=s.next, temp.next = None)
        #reverse right half linked list
        #use another two pointers to slowly filling in head

        #find mid
        s,f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next
            f = f.next
        
        #seperate into two sections
        temp = s
        s = s.next
        temp.next = None

        #s is now start of right half
        rightsec = None
        while s:
            temp = rightsec
            rightsec = s
            s = s.next
            rightsec.next = temp
        
        #rightsec is now reversed right sec

        leftsec = head

        head = leftsec
        tail = leftsec
        leftsec = leftsec.next
        #start filling head
        while rightsec: #left is shorter or equal to right
            tail.next = rightsec
            tail = tail.next
            rightsec = rightsec.next
            if leftsec:
                tail.next = leftsec
                tail = tail.next
                leftsec = leftsec.next

        return head


        
        