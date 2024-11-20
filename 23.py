# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val
        h = []
        head = tail = ListNode(0)
        for i in lists:
            if i: heapq.heappush(h, i)
        while h:
            node = heapq.heappop(h)
            tail.next = node
            tail = tail.next
            if node.next: heapq.heappush(h, node.next)
       
        return head.next   
