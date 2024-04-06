# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        visited = set()
        d = {}
        dummy = ListNode()
        dummy.next = head
        pred = dummy
        curr  = head
        while curr:
            d[curr.val] = 1 + d.get(curr.val, 0)
            curr = curr.next
        
        curr = head
        while curr:
            if d[curr.val]!=1:
                while curr and d[curr.val] !=1:
                    curr = curr.next
                pred.next = curr
                pred = curr
            else:
                pred = pred.next
            if curr is not None:   
                curr = curr.next    
        return dummy.next        