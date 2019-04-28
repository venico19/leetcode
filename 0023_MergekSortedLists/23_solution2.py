# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        if n == 0:
            return None
        elif n == 1:
            return lists[0]
        else:
            mid = n // 2
            left = self.mergeKLists(lists[:mid])
            right = self.mergeKLists(lists[mid:])
            return self.merge2Lists(left, right)
        
    def merge2Lists(self, A, B):
        dummyNode = ListNode(0)
        
        p = dummyNode
        
        while A and B:
            if A.val <= B.val:
                p.next = A
                A = A.next
            else:
                p.next = B
                B = B.next
            p = p.next
            
        if not A:
            p.next = B
        else:
            p.next = A
            
        return dummyNode.next