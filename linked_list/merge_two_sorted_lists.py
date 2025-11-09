# --------------------------------------------
# Problem:
# You are given the heads of two sorted linked lists, list1 and list2.
# Merge the two lists into one sorted linked list and return the head
# of the merged list. The new list should be made by splicing together
# the nodes of the first two lists.
# --------------------------------------------

# Definition for singly-linked list node.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# --------------------------------------------
# COMPLETE THIS FUNCTION (your code goes here)
# --------------------------------------------
def merge_two_sorted_lists(list1: Node, list2: Node) -> Node:
    # Write your code here
    dummy = Node(0)
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 or list2    
    return dummy.next
