# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def ln_to_int(l):
            res=[]
            while l:
                res.append(str(l.val))
                l=l.next
            return res
        
        l1=int(''.join(ln_to_int(l1)[::-1]))
        l2=int(''.join(ln_to_int(l2)[::-1]))
        r=list(str(l1+l2))
        r=r[::-1]
        head=ListNode()
        current=head
        for i in r:
            current.next=ListNode()
            current=current.next
            current.val=i
        return head.next