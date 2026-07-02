class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        h = n-2
        l = 0
        ans = n
        while l <= h:
            mid = l+(h-l)//2
            if arr[mid] < arr[mid+1]:
                l = mid +1
            else:
                ans = h
                h = mid -1

        return l

        