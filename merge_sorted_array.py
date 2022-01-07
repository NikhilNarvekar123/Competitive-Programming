'''
run-time: 54 ms, faster than 17.33%
mem-usage: 14.2 mb, less than 86.19%
O(n + m)
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        while n > 0:
            if m <= 0 or nums2[n - 1] >= nums1[m - 1]:
                nums1[n + m - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[n + m - 1] = nums1[m - 1]
                m -= 1
