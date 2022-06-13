"""
20220613
> https://leetcode.cn/problems/median-of-two-sorted-arrays/submissions/

执行用时：
64 ms, 在所有 Python 提交中击败了10.56%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了93.75%的用户

time cost: 12 hour
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1) + len(nums2)
        end = l // 2
        idx_1, idx_2 = 0, 0
        end_flag = ''
        new = []
        try:
            if nums1 != [] and nums2 != []:
                while idx_1 + idx_2 <= end:
                    print(idx_1, idx_2)
                    a = nums1[idx_1]
                    b = nums2[idx_2]
                    if a > b:
                        idx_2 += 1
                        new.append(b)
                    else:
                        idx_1 += 1
                        new.append(a)
                    # if idx_1 > l1:
                    #     end_flag = "1"
                    #     break
                    # elif idx_2 > l2:
                    #     end_flag = "2"
                    #     break
                print(end_flag)
                print(idx_1, idx_2)
        except IndexError:
            if idx_1 > len(nums1) - 1:
                end_flag = "1"
            elif idx_2 > len(nums2) - 1:
                end_flag = "2"

        if end_flag == '2' or nums2 == []:
            for idx in range(idx_1, end - idx_2 + 1):
                new.append(nums1[idx])
        elif end_flag == '1' or nums1 == []:
            for idx in range(idx_2, end - idx_1 + 1):
                print(idx)
                new.append(nums2[idx])
        if l % 2 == 1:
            mid = new[-1]
        else:
            mid = (new[-1] + new[-2]) * 1.0 / 2
        print(new)
        return mid


if __name__ == '__main__':
    nums1 = [2, ]
    nums2 = [1, 3, 4]
    mid = Solution().findMedianSortedArrays(nums1, nums2)
    print(mid)
