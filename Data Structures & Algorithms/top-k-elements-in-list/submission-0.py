class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dicts = defaultdict(int)

        for n in nums:
            dicts[n] += 1

        dicts = sorted(dicts.items(), key=lambda item: item[1], reverse=True)

        res = []
        for n in range(k):
            res.append(dicts[n][0])

        return res