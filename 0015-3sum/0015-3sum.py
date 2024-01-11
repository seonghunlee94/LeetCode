class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        
        for i in range(len(nums)):
            left_idx, right_idx = i + 1, len(nums) - 1
            while left_idx < right_idx:
                if nums[i] + nums[left_idx] + nums[right_idx] == 0:
                    result.add((nums[i], nums[left_idx], nums[right_idx]))
                    left_idx += 1
                    right_idx -= 1
                elif nums[i] + nums[left_idx] + nums[right_idx] < 0:
                    left_idx += 1
                else:
                    right_idx -= 1
        return result
                