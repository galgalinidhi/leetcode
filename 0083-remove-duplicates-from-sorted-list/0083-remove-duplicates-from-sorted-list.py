# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        dummy = ListNode()
        curr = dummy
        l1 = head
        curr.next = ListNode(l1.val)
        curr = curr.next
       
        l1 = l1.next
        
        while l1:
            if (l1.next and l1.next.val == l1.val) or l1.val == curr.val:
                l1 = l1.next 
            
            else:
                curr.next = ListNode(l1.val)
                curr = curr.next
                print(curr.val)
                l1 = l1.next
        return  dummy.next       