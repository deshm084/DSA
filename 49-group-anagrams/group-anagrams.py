class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagarms

        anagarm_map = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            if key not in anagarm_map:
                anagarm_map[key] = []
            anagarm_map[key].append(word)
        return list(anagarm_map.values())