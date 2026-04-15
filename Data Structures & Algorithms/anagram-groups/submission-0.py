class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for string in strs:
            sortedS = ''.join(sorted(string))
            
            if sortedS not in anagram_dict:
                anagram_dict[sortedS] = []
            
            anagram_dict[sortedS].append(string)

        return list(anagram_dict.values())