# 题目
An encoded string S is given.  To find and write the decoded string to a tape, the encoded string is read one character at a time and the following steps are taken:

    If the character read is a letter, that letter is written onto the tape.
    If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in total.

Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the decoded string.


Example 1:
```
Input: S = "leet2code3", K = 10
Output: "o"
Explanation: 
The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".

Example 2:

Input: S = "ha22", K = 5
Output: "h"
Explanation: 
The decoded string is "hahahaha".  The 5th letter is "h".

Example 3:

Input: S = "a2345678999999999999999", K = 1
Output: "a"
Explanation: 
The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".
```
 
Note:

    2 <= S.length <= 100
    S will only contain lowercase letters and digits 2 through 9.
    S starts with a letter.
    1 <= K <= 10^9
    The decoded string is guaranteed to have less than 2^63 letters.


# 解题思路及实现代码
把输入字符串按数字分离，每段字符一个record（包括字符串，字符串长度，之前生成的字符串加上此字符串的长度，加倍后的长度），正向推到所需的第k个字符的范围，然后再逆推到要求的字符返回。
```
class record:
    def __init__(self, mstr, slen, begin, end):
        self.mstr = mstr
        self.slen = slen
        self.begin = begin
        self.end = end

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def find(records, k):
    rd = records[-1]
    if rd.end >= k:
        rd2 = records[-2]
        if(rd.begin):
            k = k % rd.begin
            if(k==0):
                for i in records[::-1]:
                    if i.mstr: 
                        return i.mstr[-1]
            if(k > rd2.end):
                return rd.mstr[k-rd.begin-1]
            else:
                return find(records[:-1],k)
        else:
            return rd.mstr[-1]


class Solution:
    def decodeAtIndex(self, str: str, k: int) -> str:
        if(not hasNumbers(str)):
            return str[k-1]
        index = 0
        begin = 0
        indexbegin = 0
        rlist = [record('', 0, 0, 0)]
        for i in str:
            if '1' <= i <='9':
                mstr = str[indexbegin:index]
                slen = mstr.__len__()
                begin+=slen
                num = int(i)
                end = begin*num
                rlist.append(record(mstr, slen, begin, end))
                if(end >= k):
                    return find(rlist, k)
                begin = end
                indexbegin = index+1
            index += 1
```
- 解法参考<a href="https://leetcode.com/problems/decoded-string-at-index/discuss/156747/C%2B%2BPython-O(N)-Time-O(1)-Space">地址</a>
``` 
    def decodeAtIndex(self, S, K):
        N = 0
        for i, c in enumerate(S):
            N = N * int(c) if c.isdigit() else N + 1
            if K <= N: break
        for j in range(i, -1, -1):
            c = S[j]
            if c.isdigit():
                N /= int(c)
                K %= N
            else:
                if K == N or K == 0: return c
                N -= 1
``` 
# 总结归纳
待更新
# 吐槽篇（作者自嗨可忽略）
吐槽一下，这两天手贱，刚开始做stack类的题，第一天选了道hard，发现超时了；今天按通过率排序，选了道最低的，只有23%，类别是medium。然后就开始烧脑了。代码写到一半，发现进了一个大坑，得，重新构思吧。

这个题一看，嗯，跟昨天那道题有点像，嗯，要保存好中间过程，建一个类record保存。把输入字符串按数字分离，每段字符一个record（包括字符串，字符串长度，之前生成的字符串加上此字符串的长度，加倍后的长度），正向推到所需的第k个字符的范围，然后再逆推到要求的字符返回。嗯，思路清晰，自我感觉良好:)。~~通过一看faster 9.xx%（心凉一截，具体数字记不清了）~~刚刚为了看具体数字过去重新运行了一遍，faster than 67.68%（跟参考答案一样的速度），改了改，试了几次，发现没问题，我先去了乐会，不写了。