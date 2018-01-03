# method 1, hashtable
"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None
        
        mapping = {}
        
        p = head
        while p:
            node = RandomListNode(p.label)
            mapping[p] = node
            p = p.next

        newHead = mapping[head]
        p = head
        
        while p:
            q = mapping[p]
            
            if p.next:
                q.next = mapping[p.next]
            else:
                q.next = None
                
            if p.random:
                q.random = mapping[p.random]
            else:
                q.random = None
            
            p = p.next
        
        return newHead
