class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        first = strs[0]
        for pos, val in enumerate(first):
            for word in strs:
                if pos < len(word) and first[pos] == word[pos]:
                    continue
                else:
                    return strs[0][:pos]
        return first
            