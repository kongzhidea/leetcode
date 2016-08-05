class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        nums = []
        size = len(words)
        for w in words:
            nums += sum(1 << (ord(x) - ord('a')) for x in set(w)),
        ans = 0
        for x in range(size):
            for y in range(size):
                if not (nums[x] & nums[y]):
                    ans = max(len(words[x]) * len(words[y]), ans)
        return ans