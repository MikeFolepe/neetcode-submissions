class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:

            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else: 
                r = mid
        pivot = l

        def binarySearch(left: int, right: int) -> int:

            while left <= right:

                m = (left + right) // 2

                if target == nums[m]:
                    return m
                elif target > nums[m]:
                    left = m + 1
                else:
                    right = m - 1
            return - 1

        result = binarySearch(0, pivot - 1)

        if result != - 1:
            return result

        result = binarySearch(pivot, len(nums) - 1)

        return result

 

        