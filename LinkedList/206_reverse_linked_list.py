# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?

def reverseList(self, head):
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev

# someone solution small
# def reverseList(self, head):
#     """
#     :type head: ListNode
#     :rtype: ListNode
#     """
#     cur, prev = head, None
#     while cur:
#         cur.next, prev, cur = prev, cur, cur.next
#     return prev

# Cleaner Recursive Solution

# class Solution(object):
#     def reverseList(self, head, prev=None):
#         if not head:
#           return prev
  
#         curr, head.next = head.next, prev
#         return self.reverseList(curr, head)