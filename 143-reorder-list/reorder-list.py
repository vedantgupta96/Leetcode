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
        slow,fast = head,head.next
        while fast and fast.next:
            slow, fast = slow.next,fast.next.next
        second = slow.next #second half of the list
        slow.next = None
        prev = None #Exactly like reversing a linked list, curr is like second

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        first,second = head,prev #after above while loop, prev will be at the head of the second list that is reversed
        #second will always be shorter or equal to first list, so we run the loop on that
        while second:
            temp1,temp2 = first.next,second.next
            first.next = second
            second.next = temp1
            first,second = temp1,temp2
            




