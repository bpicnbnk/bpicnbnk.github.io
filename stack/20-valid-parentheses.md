# 题目
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
```
Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false
```

# 解题思路及实现代码
遍历输入字符串，把左括号入栈，遇到右括号，判断栈内最后一个括号是否一致对应，若正确则继续，错误则返回false。循环结束后，判断stack是否为空，不为空说明还有括号没有匹配，返回false；为空则true。
```
class Solution:
    def isValid(self, s: str) -> bool:
        slist = []
        left = ('(', '[', '{')
        sdict = {'(': ')', '[': ']', '{': '}'}
        # if(s.__len__()%2):
        #     return False
        for i in s:
            if(i in left):
                slist.append(i)
            elif(slist and i == sdict[slist[-1]]):
                slist.pop()
            else:
                return False
        return not slist
```
- 解法参考<a href="https://leetcode.com/problems/valid-parentheses/solution/">地址</a>
``` 
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
``` 
# 总结归纳
对于删除list最后一个元素，pop()与切片两种方法性能差距较大，提交时pop快很多。