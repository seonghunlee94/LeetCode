

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency_dict = Counter(nums)
        sorted_items = sorted(frequency_dict, key=frequency_dict.get, reverse=True)
        top_k_items = sorted_items[:k]
        return top_k_items
        
            