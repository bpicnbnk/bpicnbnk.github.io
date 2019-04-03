# 题目
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
```
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
```
# 解题思路及实现代码
1. 把所有节点的值放入一个list，利用Counter计数，再按key排序，最后按排序和计数结果将所有值放入新建链表
``` 
from collections import Counter
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        dnode = ListNode(0)
        dlist = []
        for node in lists:
            while(node != None):
                dlist.append(node.val)
                node = node.next
        adict = Counter(dlist)
        keys = adict.keys()
        keys = sorted(keys)
        print(keys)
        node=dnode
        for key in keys:
            v=adict[key]
            while(v != 0):
                node.next = ListNode(key)
                node=node.next
                v-=1
        return dnode.next
``` 
2. 用heapq模块，参考<a href="https://leetcode.com/problems/merge-k-sorted-lists/discuss/10849/8-lines-Python-with-generators-and-heapq.merge">地址</a>
```
class Solution:
    def mergeKLists(self, lists):
        def vals(node):
            while node:
                yield node.val
                node = node.next
        dummy = last = ListNode(None)
        for val in heapq.merge(*map(vals, lists)):
            last.next = last = ListNode(val)
        return dummy.next
```
3. queue模块，参考<a href="https://leetcode.com/problems/merge-k-sorted-lists/discuss/10511/10-line-python-solution-with-priority-queue">地址</a>
```
from queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = curr = ListNode(None)
        q = PriorityQueue()
        for idx, node in enumerate(lists):
            if node: q.put((node.val,idx,node))
        while not q.empty():
            _,idx,curr.next = q.get()
            curr=curr.next
            if curr.next: q.put((curr.next.val, idx, curr.next))
        return dummy.next
```
4. 分治思想。二分递归，可用到之前做的第21题两个有序列表合并。解法参考<a href="https://leetcode.com/problems/merge-k-sorted-lists/discuss/10919/Python-concise-divide-and-conquer-solution.">地址</a>
```
def mergeKLists(self, lists):
    if not lists:
        return 
    if len(lists) == 1:
        return lists[0]
    mid = len(lists)//2
    l = self.mergeKLists(lists[:mid])
    r = self.mergeKLists(lists[mid:])
    return self.merge(l, r)

def merge(self, l, r):
    dummy = cur = ListNode(0)
    while l and r:
        if l.val < r.val:
            cur.next = l
            l = l.next
        else:
            cur.next = r
            r = r.next
        cur = cur.next
    cur.next = l or r
    return dummy.next
```
5. 小根堆保存值和索引.解法参考<a href="https://blog.csdn.net/fuxuemingzhu/article/details/83068632">地址</a>

我们每次需要用的是K个链表头结点的最小值，所以把每个链表的头结点都放在一个小根堆里面。这样，每次弹出来的就是最小链表的值，然后根据这个值的索引去Lists中找到对应节点，拼接到末尾就行。

有人使用的弹出堆里面最小的值，然后重新生成新的节点的方式，这样不好。

另外，代码里需要注意的一个问题是，和方法一一样，需要更新链表的头结点才行，不能直接通过修改指针的方式修改，必须直接赋值更新。如果这个步骤少了的话，按照索引查找就一直获取的是老节点。

时间复杂度是O(N)，空间复杂度是O(1)。N是结果链表的长度，K是每次题目给出的链表个数。
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# heapq.heappop(heap)
#    Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised.

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(-1)
        move = head
        heap = []
        heapq.heapify(heap)
        [heapq.heappush(heap, (l.val, i)) for i, l in enumerate(lists) if l]
        while heap:
            curVal, curIndex = heapq.heappop(heap)
            curHead = lists[curIndex]
            curNext = curHead.next
            move.next = curHead
            curHead.next = None
            move = curHead
            curHead = curNext
            if curHead:
                lists[curIndex] = curHead
                heapq.heappush(heap, (curHead.val, curIndex))
        return head.next
```
# 总结归纳
这个题是21题的进阶，不难。~~上述方法中运用heapq的解法较好。我的方法再上述测试中效果看起来最好了（数据量小的原因？）。~~

~~继续找最优解，待更新。~~

解法5目前最好。思路也简单清晰。相当于每次寻找多个链表第一个节点中的最小值，添加到新链表，更新最小值节点链表（指向下一节点），继续循环。