class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        tracking = {}

        for right, value in enumerate(s):

            if value in tracking and tracking[value] >= left:
                left = tracking[value] + 1

            tracking[value] = right

            max_length = max(max_length, right - left + 1)
        return max_length