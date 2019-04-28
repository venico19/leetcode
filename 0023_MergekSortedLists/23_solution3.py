# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        while len(lists) > 1:
            newLists = []
            k = 0
            while k + 1 < len(lists):
                newLists.append(self.merge2Lists(lists[k], lists[k+1]))
                k += 2
            if k < len(lists):
                newLists.append(lists[k])
            lists = newLists
            
        return lists[0]
        
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