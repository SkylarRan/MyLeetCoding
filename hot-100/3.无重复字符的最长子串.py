#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
from queue import Queue
 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = Queue()
        maxlength = 0
        for i in s:
            if i not in q:
                q.put(i)
                if q.qsize() > maxlength:
                    maxlength = q.qsize()
            else:
                while True: 
                    if i == q.get():
                        break

        
# @lc code=end

