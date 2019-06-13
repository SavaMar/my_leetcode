# Given a singly linked list, determine if it is a palindrome.

# Input: 1->2
# Output: false
# Example 2:

# Input: 1->2->2->1
# Output: true

# Could you do it in O(n) time and O(1) space?

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        a =[]
        while head:
            a.append(head.val)
            head = head.next
        return a == a[::-1]