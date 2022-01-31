from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            for j,num2 in enumerate(nums):
                if i == j:
                    continue
                if num1 + num2 == target:
                    return [i, j]

solutions = Solution()
answer = solutions.twoSum([2,7,11,15],9)
print(answer)
answer = solutions.twoSum([3,2,4],6)
print(answer)
answer = solutions.twoSum([3,3],6)
print(answer)