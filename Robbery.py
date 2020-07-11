class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        def lineRob(nums):
            if not nums:
                return 0
            n=len(nums)
            if n<2:
                return nums[0]
            dp=[0]*n
            dp[0]=nums[0]
            dp[1]=max(nums[0],nums[1])
            for i in range(2,n):
                dp[i]=max(dp[i-1],dp[i-2]+nums[i])
            return dp[n-1]
        return max((nums[0]+lineRob(nums[2:-1])),lineRob(nums[1:]))
vall = Solution()
Room=list(map(int,input().split()))
print(vall.rob(Room))
