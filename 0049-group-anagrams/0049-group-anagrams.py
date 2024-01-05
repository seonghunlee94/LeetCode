class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = {}
        
        sorted_word = [sorted(word) for word in strs]


        for i in range(len(sorted_word)):
            word = ''.join(sorted_word[i])
            if word in group_dict:
                group_dict[word].append(strs[i])
            else:
                group_dict[word] = [strs[i]]

        return list(group_dict.values())