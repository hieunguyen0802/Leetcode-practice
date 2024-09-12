# set max sub at nums[0], curSum = 0. iterate thru the array, check if the curSum is less than 0, then reset the curSum. Otherwise keep accumulating the curSum. Find the max between curSum and maxSub. 
# time and space: 0(n)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0] 
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(curSum, maxSub)    
        return maxSub
