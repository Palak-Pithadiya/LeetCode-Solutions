# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
:type lists: List[Optional[ListNode]]
:rtype: Optional[ListNode]
"""

import heapq

class Solution:
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        curr = dummy
        min_heap = []

        for i, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, i, l))

        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            curr.next = ListNode(val)
            curr = curr.next
            
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next
