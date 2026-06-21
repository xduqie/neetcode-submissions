class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for each in word:
                count[ord(each)-ord("a")]+=1
            hash[tuple(count)].append(word)

        return list(hash.values())