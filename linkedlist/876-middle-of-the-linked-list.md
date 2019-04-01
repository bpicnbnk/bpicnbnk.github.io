# 题目
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

Example 1:
```
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
```
Example 2:
```
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
```
 
Note:

    The number of nodes in the given list will be between 1 and 100.

# 解题思路
遍历得到链表元素数量，算出中间值，遍历到中间节点返回
# 实现代码
```
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        i = 1
        q = head
        while q.next != None:
            i += 1
            q = q.next
        middle = i//2
        while(middle != 0):
            middle -= 1
            head = head.next
        return head
```
- 其他解法参考<a href="https://leetcode.com/problems/middle-of-the-linked-list/solution/">地址</a>
- 解法1
```
class Solution(object):
    def middleNode(self, head):
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) // 2]#此处原始代码有误
```
- 解法2
```
class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```
# 总结归纳
此题链表节点数量在1-100之间，比较少，思路也简单。划水的一题。上述解法运行时间空间均接近，其它解法中也学到了些东西。对于参考解法，解法一空间复杂度较大，他是用list实现的，也可以用dict。解法2应该是python中最优雅的吧，还没看到更好的，数据量大的话效果应该更好。看了看其他语言的解法，Java中有些运行时间0ms的解法？？？思路与上面几个解法一致，运行空间倒是python的3倍，其他没发现有什么特别的地方。
