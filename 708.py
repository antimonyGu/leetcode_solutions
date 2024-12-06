"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # edge case: empty list
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        
        curr = head
        while curr.next != head:
            # insert in normal position
            if curr.val <= insertVal <= curr.next.val:
                break

            # insert in link position
            if (curr.val > curr.next.val) and (curr.val < insertVal or curr.next.val > insertVal):
                break
            
            curr = curr.next
        
        insert_node = Node(insertVal, next=curr.next)
        curr.next = insert_node
        return head