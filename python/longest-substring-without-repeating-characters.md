# longest-substring-without-repeating-characters.py

> 给定一个字符串 `s` ，请你找出其中不含有重复字符的 **最长子串** 的长度。
>
> https://leetcode.cn/problems/longest-substring-without-repeating-characters/



**结果：**$\star\star\star$

```bash
20220612
> https://leetcode.cn/problems/longest-substring-without-repeating-characters/

执行用时：60 ms, 在所有 Python3 提交中击败了84.22%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了96.26%的用户

time cost: 10 min
```



**代码：**

```python
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
```



**思路**

遍历序列$s$的每个字符$str$

初始化子序列$sub\_s$，如果在$sub\_s$中能找到$str$，则说明该阶段的子序列查找完毕

以$str$为标志分割$sub\_s$，取后面的取代$sub\_s$

**key:**这里截取后的$sub\_s$要加上$str$，不然会漏掉这个字符

遍历完$s$结束程序
