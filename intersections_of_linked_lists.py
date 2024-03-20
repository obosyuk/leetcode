# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        listA = []
        pointer = headA
        while pointer is not None:
            listA.append(pointer)
            pointer = pointer.next
        listA.reverse()

        listB = []
        pointer = headB
        while pointer is not None:
            listB.append(pointer)
            pointer = pointer.next
        listB.reverse()

        intersectNode = None
        for idx in range(max(len(listA), len(listB))):
            if idx <= len(listA) - 1 and idx <= len(listB) - 1 and listA[idx] == listB[idx]:
                intersectNode = listA[idx]
            else:
                break

        return intersectNode


