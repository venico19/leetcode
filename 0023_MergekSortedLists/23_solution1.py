# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        candidates = []
        for i in range(len(lists)):
            if lists[i]:
                node = lists[i]
                heapq.heappush(candidates, (node.val, i, node))
        
        dummyNode = ListNode(0)
        head = dummyNode
        while candidates:
            i, smallestNode = heapq.heappop(candidates)[1:]
            if smallestNode.next:
                heapq.heappush(candidates, (smallestNode.next.val, i, smallestNode.next))
            head.next = smallestNode
            head = head.next
            
        return dummyNode.next