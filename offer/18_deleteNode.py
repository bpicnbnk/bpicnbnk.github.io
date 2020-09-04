from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        pre = head
        v = head
        while head:
            if head.val == val:
                if pre.val == val:
                    return head.next
                else:
                    pre.next = head.next

            pre = head
            head = head.next

        return v


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        v = head
        if head:
            if head.val == val:
                return head.next

            while head.next:
                if head.next.val == val:
                    head.next = head.next.next
                    break
                else:
                    head = head.next
        return v

    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return head
        if head.val == val:
            return head.next

        head.next = self.deleteNode(head.next, val)
        return head


s = Solution()
nums = [-1, 2, 1, -4]
result = s.threeSumClosest(nums)
print(result)
