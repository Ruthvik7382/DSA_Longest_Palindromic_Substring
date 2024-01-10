#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def preprocess(s):
            if not s:
                return "^$"
            result = "^"
            for char in s:
                result += "#" + char
            result += "#$"
            return result
        t = preprocess(s)
        n = len(t)
        p = [0] * n
        center, right = 0, 0
        for i in range(1, n - 1):
            if i < right:
                mirror = 2 * center - i
                p[i] = min(right - i, p[mirror])

            # Attempt to expand palindrome centered at i
            while t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1

            # If palindrome centered at i expands past right,
            # adjust center and right based on expanded palindrome.
            if i + p[i] > right:
                center, right = i, i + p[i]

        max_length, max_center = max((n, i) for i, n in enumerate(p))
        start = (max_center - max_length) // 2
        return s[start:start + max_length]


# In[2]:


s = "babad"
solution = Solution()
result = solution.longestPalindrome(s)


# In[3]:


result


# In[ ]:




