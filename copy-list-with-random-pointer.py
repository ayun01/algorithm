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

    # method 2:
    # 第一遍扫的时候巧妙运用next指针， 开始数组是1->2->3->4  。 然后扫描过程中 先建立copy节点 1->1`->2->2`->3->3`->4->4`, 
    # 然后第二遍copy的时候去建立边的copy， 拆分节点, 一边扫描一边拆成两个链表，这里用到两个dummy node。第一个链表变回  1->2->3 , 
    # 然后第二变成 1`->2`->3`
    # http://www.jiuzhang.com/solution/copy-list-with-random-pointer/
    class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return head
        
        self.expendList(head)
        self.copyRandomLink(head)
        newHead = self.splitList(head)
        return newHead
        
    # assert head is not None
    def expendList(self, head):
        p = head
        while p:
            next = p.next
            node = RandomListNode(p.label)
            node.next = p.next
            p.next = node
            
            p = next
    
    # assert head is not None
    def copyRandomLink(self, head):
        p = head
        while p and p.next:
            next = p.next.next
            if p.random:
                p.next.random = p.random.next
            else:
                p.next.random = None
                
            p = next
    
    # assert head is not None and at least two nodes
    def splitList(self, head):
        p = head
        newHead = head.next
        q = newHead
        while p and p.next:
            next = p.next.next
            
            if next:
                q.next = next.next
                p.next = next
            
                p = next
                q = q.next
            else:
                q.next = None
                p.next = None
        
        return newHead
