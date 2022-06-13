"""
20220612
> https://leetcode.cn/problems/longest-substring-without-repeating-characters/

执行用时：60 ms, 在所有 Python3 提交中击败了84.22%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了96.26%的用户

time cost: 10 min
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        sub_s = ''
        for str in s:
            idx = sub_s.find(str)
            if idx != -1:
                sub_s = sub_s.split(str)[1]
            sub_s += str
            temp_l = len(sub_s)
            if temp_l > max_l:
                max_l = temp_l
            # print(sub_s)
        return max_l


if __name__ == '__main__':
    s = "aab"
    # s = "pwwkew"
    l = Solution().lengthOfLongestSubstring(s)
    print(l)
