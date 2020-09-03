from typing import List
import re


class Solution:
    def replaceSpace(self, s: str) -> str:
        p = re.compile(r'\s')
        return re.sub(p, '%20', s)


s = Solution()
p = "We are happy."
result = s.replaceSpace(p)
print(result)
