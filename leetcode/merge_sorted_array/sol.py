class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        q = m + n - 1
        """
        Keep one pointer each to the last element of each array.
        Also keep one pointer to denote the place where the element should be 
        copied.
        Copy the bigger element and decrement the appropriate pointer.
        """
        while (p1 >= 0 and p2 >= 0):
            if (nums1[p1] > nums2[p2]):
                nums1[q] = nums1[p1]
                p1 -= 1
            else:
                nums1[q] = nums2[p2]
                p2 -= 1
            q -= 1
            
        # copy the remaining nums2 if required
        while (p2 >= 0):
            nums1[q] = nums2[p2]
            p2 -= 1
            q -= 1
