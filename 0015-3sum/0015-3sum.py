from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result_array = []
        n = len(nums)
        
        for i in range(n - 2):
            # skip if nums[i] is same as prev num since sorted to avoid duplicate triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # left pointer in inner loop ==> mid since outer loop i points to the left!
            mid = i + 1
            right = n - 1

            while mid < right:
                total = nums[i] + nums[mid] + nums[right]

                if total == 0:
                    result_array.append([nums[i], nums[mid], nums[right]])
                    mid += 1
                    right -= 1
                    # skip duplicate elements to the right of the current mid pointer
                    while mid < right and nums[mid] == nums[mid - 1]:
                        mid += 1
                    # skip duplicate elements to the left of the current right pointer
                    while mid < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    mid += 1
                else:
                    right -= 1

        return result_array


# Maintaining Sorted Order: The code uses the two-pointer technique to maintain a sorted order of exploration. Since the array is sorted, when the sum of the three elements is less than zero (total < 0), it means that the current triplet's sum is too small, and we need a larger value. Therefore, we increment the left pointer to explore larger values. Conversely, when the sum is greater than zero (total > 0), the current triplet's sum is too large, so we decrement the right pointer to explore smaller values. By doing so, the algorithm covers all possible combinations without missing any valid triplets.
