# 题目
Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

    push(int x), which pushes an integer x onto the stack.
    pop(), which removes and returns the most frequent element in the stack.
        If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.
```
class FreqStack:

    def __init__(self):
        

    def push(self, x: int) -> None:
        

    def pop(self) -> int:
       

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
```

Example 1:
```
Input: 
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -> returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -> returns 5.
The stack becomes [5,7,4].

pop() -> returns 4.
The stack becomes [5,7].
```

Note:

    Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
    It is guaranteed that FreqStack.pop() won't be called if the stack has zero elements.
    The total number of FreqStack.push calls will not exceed 10000 in a single test case.
    The total number of FreqStack.pop calls will not exceed 10000 in a single test case.
    The total number of FreqStack.push and FreqStack.pop calls will not exceed 150000 across all test cases.


# 解题思路及实现代码
代码leetcode验证，在30/37时超时，超时时输入数据较大。
```
from collections import Counter
class FreqStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            dict = Counter(self.stack)
            ndict = sorted(dict.items(), key=lambda item: item[1])
            d, num = ndict[-1]
            indexndict = -2
            l = [d]
            len = ndict.__len__()-1
            while(len):
                if(num == ndict[indexndict][1]):
                    l.append(ndict[indexndict][0])
                    indexndict -= 1
                    len -= 1
                else:
                    break
            
            t = self.stack[::-1]
            for i in t:
                if(i in l):
                    remove=i
                    break
            t.remove(remove)
            self.stack = t[::-1]
            return remove
```
# 参考解法
## 一 <a href="https://leetcode.com/problems/maximum-frequency-stack/discuss/220134/Python-O(1)-time-360ms-beats-100">地址</a>
1. self.freq2Val maps frequencies to its corresponding element.
2. self.val2Freq is a simple counter, similar to collections.Counter() mapping elements to their frequencies.
3. self.best holds the current highest frequency.
``` 
class FreqStack:
    def __init__(self):
        self.freq2Val = collections.defaultdict(list)
        self.val2Freq = dict()
        self.best = 0

    def push(self, x):
        self.val2Freq[x] = self.val2Freq.get(x, 0) + 1
        self.freq2Val[self.val2Freq[x]].append(x)
        self.best = max(self.best, self.val2Freq[x])

    def pop(self):
        valsWithBestFrequency = self.freq2Val[self.best]
        popped = valsWithBestFrequency.pop()
        self.best -= not valsWithBestFrequency
        self.val2Freq[popped] -= 1
        return popped
``` 
4. self.best -= not valsWithBestFrequency decreases the current best frequency when there are no more elements that have this frequency.
# 总结归纳
这个题有点难度。pop()时返回并移除出现频率最高的元素，若出现多个相同频率则选择入栈最晚的元素。按照我的思路，push将元素压栈，pop查找所需元素会超时；要保证时间复杂度达到要求就需要每次执行push，pop时更新的元素及其频率变化，这种数据构造有点难度，可参考解法一。