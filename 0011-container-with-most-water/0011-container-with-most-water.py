class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            max_area = max(area, max_area)

            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1

        return max_area

        # TIME LIMIT ACCESS (ON^2)
        # max_area = 0
        # for line in range(len(height) - 1):
        #     # line + 1 to ... len(height) since starting from 1
        #     for next_line in range(line+1, len(height)):
        #         area = min(height[line], height[next_line]) * (next_line - line)
        #         max_area = max(area, max_area)       
        # return max_area