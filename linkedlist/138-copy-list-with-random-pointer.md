# 题目
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
Input:
```
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
```
Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
Note:

    You must return the copy of the given head as a reference to the cloned list.

# 解题思路和实现代码
1. 调用copy模块的deepcopy()

```
import copy
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        return copy.deepcopy(head)
```
2. 新建链表，循环给新链表复制节点的val，next，并将两个链表每个节点分别存入两个list。循环结束后，再循环将random利用list补全。
```
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        newnode = Node(None, None, None)

        pnew = newnode
        phead = head
        listhead = []
        listnew = []
        while(phead != None):
            listhead.append(phead)
            pnew.next = Node(phead.val, None, None)
            pnew = pnew.next
            listnew.append(pnew)
            phead = phead.next

        pnew = newnode.next
        phead = head
        while(phead != None):
            if phead.random:
                pnew.random = listnew[listhead.index(phead.random)]
            phead = phead.next
            pnew = pnew.next

        return newnode.next
```
3. 2的思路中list换为dict 
- 解法参考<a href="https://leetcode.com/problems/copy-list-with-random-pointer/discuss/261633/Python3-2-pass-solution-beats-100">地址</a>
``` 
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy = Node(-1, None, None)

        cur = head
        newcur = dummy
        nodemap = {}
        while cur:
            newNode = Node(cur.val, None, None)
            newcur.next = newNode
            newcur = newcur.next

            nodemap[cur] = newcur
            cur = cur.next

        cur = head
        newcur = dummy.next
        while cur:
            if cur.random:
                newcur.random = nodemap[cur.random]
            cur = cur.next
            newcur = newcur.next

        return dummy.next
``` 
4. 最优解参考<a href="https://leetcode.com/problems/copy-list-with-random-pointer/discuss/259899/Python-O(n)-100-faster-than-others">地址</a>
   思路可参考<a href="https://www.cnblogs.com/zuoyuan/p/3745126.html">地址</a>，自己画图也很好理解
   
The idea is to associate the original node with its copy node in a single linked list. In this way, we don't need extra space to keep track of the new nodes.
The algorithm is composed of the follow three steps which are also 3 iteration rounds.

1. Iterate the original list and duplicate each node. The duplicate of each node follows its original immediately.
2. Iterate the new list and assign the random pointer for each duplicated node.
3. Restore the original list and extract the duplicated nodes.
参考 <a href="https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491/A-solution-with-constant-space-complexity-O(1)-and-linear-time-complexity-O(N)">地址</a>
```
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        <!-- 复制新节点到旧节点后，是一个新链表。新节点中复制temp.next保证链表连续 -->
        temp = head
        while temp != None:
            node = Node(temp.val, temp.next, None)
            temp.next = node
            temp = temp.next.next
    
        temp1 = head
        while temp1 != None:
            if temp1.random != None:
                #新旧链表相同节点相邻，新链表的random是旧链表random.next
                temp1.next.random = temp1.random.next
            temp1 = temp1.next.next
        
        temp1 = head
        final = head.next
        temp2 = head.next
        while temp1 != None:
            #保持原链表不变
            temp1.next = temp1.next.next

            temp1 = temp1.next
            if temp2.next != None:
                temp2.next = temp1.next
            
            temp2 = temp2.next
        
        return final
```
# 总结归纳
- 第一种解法当开胃菜吧。可以用。
- 第二，三种解法适合数据量小的情况。第三种解法没想到如何构建字典，参考解法给了一个好的示例
- 第四种解法比较完美了。
