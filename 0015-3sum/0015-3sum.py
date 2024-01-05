class Solution:
                        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        unique_triplets = set()
        total_sum = 0

        for i in range(len(nums)):
            left_idx, right_idx = i + 1, len(nums) - 1

            while left_idx < right_idx:
                total_sum = nums[i] + nums[left_idx] + nums[right_idx]

                if total_sum == 0:
                    unique_triplets.add((nums[i], nums[left_idx], nums[right_idx]))
                    left_idx += 1
                    right_idx -= 1
                elif total_sum < 0:
                    left_idx += 1
                else:
                    right_idx -= 1
        return unique_triplets


