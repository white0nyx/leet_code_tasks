from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not self:
            return ""

        min_word = min(strs, key=len)
        for i in range(len(min_word)):
            for s in strs:
                if s[i] != min_word[i]:
                    return min_word[:i]

        return min_word


print(Solution().longestCommonPrefix(["reflower", "flow", "flight"]))
