class Solution:
                        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 정렬
        nums = sorted(nums)
        
        # 정렬 시키면, [-4, -1, -1, 0, 1, 2]
        # print(nums)
        left_idx = 1
        right_idx = len(nums)-1 
        answer = set()
        sum = 0
        
        # two pointer로 left right. 기준 인덱스.
        for i in range(0, len(nums) -2):
            
            while left_idx != right_idx:

                sum = nums[i] + nums[left_idx] + nums[right_idx]
                if  sum < 0:
                    left_idx += 1
                elif sum > 0:
                    right_idx -= 1
                else:
                    answer.add((nums[i],nums[left_idx],nums[right_idx]))
                    left_idx += 1
            left_idx = i + 2
            right_idx = len(nums)-1

        return answer
        
        
        
        # left - right가 같은 인덱스를 가리키면 break
        # 삼중합이 0보다 크거나 같으면 left += 1
        # 작으면 right -= 1
        # 
        
        
        
        
        # output [[-1,-1,2],[-1,0,1]]


