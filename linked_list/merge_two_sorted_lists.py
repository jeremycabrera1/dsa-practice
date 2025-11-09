# Problem:
# Given the head of a singly linked list, return the value of the middle node.
# If there are two middle nodes, return the value of the second middle node.

class Node:
    def __init__(self, val=0, next=None):
        self.val = val        
        self.next = next  


def middle_of_linked_list(head:Node) -> int:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next 
        slow = slow.next
    return slow.val
