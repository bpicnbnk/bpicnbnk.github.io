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
3. queue模块

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
# 总结归纳
这个题是21题的进阶，不难。上述方法中运用heapq的解法较好。我的方法再上述测试中效果看起来最好了（数据量小的原因？）。
继续找最优解，待更新。