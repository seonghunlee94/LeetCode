

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
        
        # frequency_dict = Counter(nums)
        # top_k_items = [item for item, _ in frequency_dict.most_common(k)]
        # return top_k_items
        
        # frequency_dict = Counter(nums)
        # sorted_items = sorted(frequency_dict, key=frequency_dict.get, reverse=True)
        # top_k_items = sorted_items[:k]
        # return top_k_items
        
        
            