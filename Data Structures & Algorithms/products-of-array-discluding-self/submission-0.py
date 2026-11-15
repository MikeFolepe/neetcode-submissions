class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        left = [1] * n
        right = [0] * n
        right[n-1] = 1
        prefix = 1
        for i in range(n):
            left[i] = prefix
            prefix *= nums[i]
        for i in reversed(range(n-1)):
            right[i] = right[i+1] * nums[i+1]
        for i in range(n):
            ans.append(left[i] * right[i])
        return ans

        