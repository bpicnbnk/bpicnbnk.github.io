# 题目
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```
# 解题思路
注意到两个链表是有序的，接下来就简单了。创建新链表，若两个链表为空，直接返回；若其中一个不为空，则将另一个链表节点指向新链表返回；均不空，遍历两个链表，按照题目规则，比较大小，加入新链表，遍历过程中可能出现第二种情况。
# 实现代码
```
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ln = ListNode(0)
        head = ln
        node1 = l1
        node2 = l2
        while(node1 != None or node2 != None):
            if node2 == None:
                head.next = node1
                break
            while(node2 != None):
                if node1 == None:
                    head.next = node2
                    node2 = None
                    break
                if node1.val == node2.val:
                    head.next = node1
                    node1 = node1.next
                    head = head.next
                    head.next = node2
                    node2 = node2.next
                elif node1.val > node2.val:
                    head.next = node2
                    node2 = node2.next
                else:
                    head.next = node1
                    node1 = node1.next
                head = head.next
        return ln.next
```
- 其他好的解法参考<a href="https://blog.csdn.net/coder_orz/article/details/51529359" target="_blank">地址</a>
```  
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        head = cur = ListNode(0) 
        while l1 and l2: 
            if l1.val < l2.val: 
                cur.next = l1 
                l1 = l1.next 
            else: 
                cur.next = l2 
                l2 = l2.next
            cur = cur.next 
        cur.next = l1 or l2 
        return head.next
```
# 遇到的问题
- 边界条件：链表问题在开始，结束和中间过程中注意判断空值。
# 总结归纳
链表问题最近接触比较多，可以实现功能，但是代码繁琐（难以直视）。边界界定和条件判断情况方面需多思考，写的更清晰简练。第二段代码开头的链表判空和结尾的补全，优秀啊。