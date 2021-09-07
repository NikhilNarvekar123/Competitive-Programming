'''
run-time: 161 ms, faster than 9.05%
mem-usage: 14.5 MB, less than 80.76%

still meets criteria of problem as efficiency is O(n + m) for required < O(log(m+n))
'''

class Solution:
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        i = 0
        j = 0
        sortedArr = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sortedArr.append(nums1[i])
                i += 1
            else:
                sortedArr.append(nums2[j])
                j += 1
        
        if i < len(nums1):
            for idx in range(i, len(nums1)):
                sortedArr.append(nums1[idx])
        
        if j < len(nums2):
            for idx in range(j, len(nums2)):
                sortedArr.append(nums2[idx])
        
        if len(sortedArr) % 2 != 0:
            return float(sortedArr[len(sortedArr) // 2])
        else:
            leftVal = sortedArr[(len(sortedArr) // 2) - 1]
            rightVal = sortedArr[(len(sortedArr) // 2)]
            return (leftVal + rightVal) / 2
        
        
