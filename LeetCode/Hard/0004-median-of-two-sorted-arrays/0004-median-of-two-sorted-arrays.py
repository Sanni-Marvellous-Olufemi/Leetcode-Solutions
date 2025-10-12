class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        odd = True if ((m+n) % 2 == 1) else False
        k = ((m+n)//2)+1 if odd else (m+n)//2
        up, down = 0, 0
        
        if not n:
            return nums1[k-1] if odd else (nums1[k-1] + nums1[k])/2

        if not m:
            return nums2[k-1] if odd else (nums2[k-1] + nums2[k])/2

        while k > 1 and up < m and down < n:
            curr_up, curr_down = up, down

            if up + k//2 < m:
                curr_up += k//2 - 1
            if down + k//2 < n:
                curr_down += k//2 - 1

            if nums1[curr_up] > nums2[curr_down]:
                k -= abs((curr_down - down) + 1)
                down = curr_down + 1    
            else:
                k -= abs((curr_up - up) + 1)
                up = curr_up + 1
                

        if up < m and down < n:
            mid1 = nums1[up] if down == n-1 else min(nums1[up], nums2[down + 1])
            mid2 = nums2[down] if up == m-1 else min(nums2[down], nums1[up + 1])
        else:
            mid1 = nums1[up + k - 1] if up < m else nums2[down + k]
            mid2 = nums2[down + k - 1] if down < n else nums1[up + k]


        return min(mid1, mid2) if odd else (mid1 + mid2)/2
                
            

            

