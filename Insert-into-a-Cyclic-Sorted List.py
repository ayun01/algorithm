class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def insertCircleListNode(self, head, val):
        Node = ListNode(val)
        # empty head
        if head is None:
            head = Node

        # one node
        if head.next is None:
            Node.next = head.next
            head.next = Node

        # in the mid
        p = head
        while p.next != head:
            if p.next.val >= val:
                Node.next = p.next
                p.next = Node
            else:
                p = p.next

        # last node
        if p.next == head and val > p.val:
            Node.next = p.next
            p.next = Node

        return head
