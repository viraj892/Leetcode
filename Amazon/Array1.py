
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 1:
            return 0
        elif len(s) == 0:
            return -1
        else:
            s = list(s)
            us = set(s)
            min_index = len(s) - 1
            unique_exists = False
            for c in us:
                if s.count(c) == 1:
                    unique_exists = True
                    min_index = min(s.index(c), min_index)
            if not unique_exists:
                return -1
            return min_index


print(Solution().firstUniqChar("cccaabadb"))
