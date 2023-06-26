class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i, num in enumerate(nums):
            for j, nextNum in enumerate(nums[i + 1:]):
                if num + nextNum == target:
                    answer.append(i)
                    answer.append(j + i + 1)
                    return answer
        return answer