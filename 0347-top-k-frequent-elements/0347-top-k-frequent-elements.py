class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        # Counter한 후 dict와 유사한 형태로 리턴 
        frequent_dict = Counter(nums)
        
        top_k_items = [item for item, _ in frequent_dict.most_common(k)]
            
        return top_k_items
            