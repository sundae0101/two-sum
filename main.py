from typing import List
 def twoSum(nums: List[int], target: int) -> List[int]:
     N = len(nums) - 1
     for i in range(N):
         for j in range(i+1, N):
             if (nums[i] + nums[j] == target):
                 return [i, j]