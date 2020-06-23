from typing import List
from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        keys = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        words = []
        for c in digits:
            words.append(keys[c])

        words = list(product(*words))
        final_words = []
        for word in words:
            final_words.append("".join(map(str, word)))
        return final_words


print(Solution().letterCombinations("23"))
