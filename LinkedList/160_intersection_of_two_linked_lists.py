import pdb

class Node(object):
  def __init__(self,x):
    self.val = x
    self.next = None

class LinkedList(object):
  def __init__(self,head):
    self.head = head
  def append(self, new_node):
    if self.head:
      current = self.head
      while current.next != None:
        current = current.next
      current.next = new_node   
    else:
      self.head = new_node
  def show_all(self):
    # print("Hohoh")
    a = []
    current = self.head
    a.append(current.val)
    while current.next:
      a.append(current.next.val)
      current = current.next
    return a

class Solution(object):
  def getIntersectionNode(self, headA, headB):
        ptA, ptB, jumpToNext = headA, headB, False
        j = 0
        # pdb.set_trace()
        while ptA and ptB:
            if ptA == ptB:
                print("ptA == ptB")
                print("j: ", j)
                return ptA.val
            ptA, ptB = ptA.next, ptB.next
            if not ptA and not jumpToNext:
                j += 1
                ptA, jumpToNext = headB, True
            if not ptB:
                j += 1
                ptB = headA
        return None

# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         if not headA or not headB:
#             return None
#         topA = headA
#         topB = headB

#         topAlength = 1
#         topBlength = 1

#         while topA.next:
#             topAlength += 1
#             topA = topA.next

#         while topB.next:
#             topBlength += 1
#             topB = topB.next

#         small = headA if topAlength <= topBlength else headB
#         buff = abs(topAlength - topBlength)

#         current = headA if topAlength > topBlength else headB

#         for i in range(0, buff):
#             current = current.next

#         hmmm = topAlength if topAlength > topBlength else topBlength

#         for i in range(0, hmmm):
#             if(small == current):
#                 return small
#             small = small.next
#             current = current.next
#         return None
       


a = Node(4)
a1 = Node(1)
a2 = Node(8)
a3 = Node(4)
a4 = Node(5)
# a = Node(1)
# a1 = Node(3)

b = Node(5)
c = Node(12)
cc = Node(7)
b1 = Node(0)
b2 = Node(1)
# 
# b = Node(2)
# b1 = Node(4)

# first LL
ll1 = LinkedList(a)
ll1.append(a1)
ll1.append(a2)
ll1.append(a3)
ll1.append(a4)

# second LL
# ll2 = LinkedList(a)
ll2 = LinkedList(b)
ll2.append(c)
ll2.append(cc)
ll2.append(b1)
ll2.append(b2)
ll2.append(a2)


print("L1: ", ll1.show_all())
print("L2: ", ll2.show_all())
# print(ll1.head) 

b = Solution()

print(b.getIntersectionNode(ll1.head, ll2.head))



# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         """
#         :type head1, head1: ListNode
#         :rtype: ListNode
#         """
#         topA = headA
#         topB = headB
#         while topA.next:
#             while topB.next:
#                 if topA==topB:
#                     return topA
#                 else:
#                     topB = topB.next
#             topA = topA.next
#             topB = headB