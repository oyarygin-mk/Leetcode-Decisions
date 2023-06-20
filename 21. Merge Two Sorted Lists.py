from typing import Optional

list1 = [2, 3, 8, 10, 12]
list2 = [1, 2, 3, 7, 8]

res = []

i = 0
j = 0

while i < len(list1) or j < len(list2):
    if i == len(list1):
        while j < len(list2):
            res.append(list2[j])
            j += 1
        break
    if j == len(list2):
        while i < len(list1):
            res.append(list1[i])
            i += 1
        break

    if (list1[i] > list2[j]):
        res.append(list2[j])
        j += 1
    else:
        res.append(list1[i])
        i += 1
print(res)

###############################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = []

        i = list1
        j = list2  

        while (i is not None) or (j is not None):
            if i is None:
                while j is not None:
                    res.append(j.val)
                    j = j.next
                break
            if j is None:
                while i is not None:
                    res.append(i.val)
                    i = i.next
                break

            if (i.val > j.val):
                res.append(j.val)
                j = j.next
            else:
                res.append(i.val)
                i = i.next
        if not res:
            return None

        head = ListNode(val=res[0], next=None)
        cur = head

        for i in res:
            new = ListNode(val=i, next=None)
            cur.next = new
            cur = new
        return head.next

