# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        done = False
        merged_head, merged_tail = None, None

        while not done:
            minimum, list_idx = None, None          
            for idx, list_node in enumerate(lists):                                
                if list_node is not None and (minimum is None or list_node.val <= minimum):                
                    minimum, list_idx = list_node.val, idx
            
            if list_idx is None:
                done = True
            else:
                temp = lists[list_idx].next
                if merged_head is None:
                    merged_head = lists[list_idx]
                    merged_tail = lists[list_idx]
                else:                
                    merged_tail.next = lists[list_idx]
                    merged_tail = merged_tail.next
                
                lists[list_idx] = temp
        
        return merged_head
    