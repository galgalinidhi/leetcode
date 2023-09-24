# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        prev = None
        slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        left = head
        right = prev
        while right:
            temp1= left.next
            temp2 = right.next
            left.next = right
            right.next = temp1
            left = temp1
            right = temp2
            
         
        
         
             
                
            
        
                
            
            
            
            
  
            
            
        