class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0]*n
        res = 0
        prefix_sum[0] = nums[0]
        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        for i in range(n-1):
            left_sum = prefix_sum[i]
            right_sum = (prefix_sum[n-1] - prefix_sum[i])
            if(abs(left_sum-right_sum) % 2 == 0):
                res += 1
        return res